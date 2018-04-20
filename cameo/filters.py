import cv2
import numpy as np

""" 卷积滤波器的基类 """
class VConvolutionFilter(object):
    """ 针对图像的一般的卷积滤波器, 各种特定滤波器的基类 """

    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        """ 对一张BGR或灰度的源图像应用特定的滤波器 """
        cv2.filter2D(src, -1, self._kernel, dst)


""" 锐化滤波器
 @extend VConvolutionFilter
 """
class SharpenFilter(VConvolutionFilter):
    """ 1 像素半径的锐化滤波器 """

    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])
        super(SharpenFilter, self).__init__(kernel)


""" 边缘检测滤波器
 @extend VConvolutionFilter
 """
class FindEdgesFilter(VConvolutionFilter):
    """ 1 像素半径的边缘检测滤波器 """

    def __init__(self):
        # 通过自定义核的简单卷积和检测效果较差
        kernel = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])
        super(FindEdgesFilter, self).__init__(kernel)

    def strokeEdgesOriginBg(self, src, dst, blurKsize = 7, edgeKsize = 5):
        """ 在源图像基础上描绘出黑色的边缘 """

        # 若要关闭模糊效果, 可以将blurKsize的值设为3以下
        if blurKsize >= 3:
            blurredSrc = cv2.medianBlur(src, blurKsize)
            graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
        else:
            graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        # 边缘检测函数, 它会产生明显的边缘线条, 灰度图像更是如此
        cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize = edgeKsize)

        # 归一化系数, 将原来的 黑色背景、白色边缘图像 转换为 黑色边缘、白色背景图像
        normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)

        # 通道拆分
        channels = cv2.split(src)

        # 归一化系数 乘以 源图像 以便能将边缘变黑
        for channel in channels:
            channel[:] = channel * normalizedInverseAlpha

        # 通道合并
        cv2.merge(channels, dst)

    def strokeEdgesBlackBg(self, src, blurKsize = 7, edgeKsize = 5):
        """ 将源图像背景变为黑色, 并描绘出白色的边缘 """

        # 若要关闭模糊效果, 可以将blurKsize的值设为3以下
        if blurKsize >= 3:
            blurredSrc = cv2.medianBlur(src, blurKsize)
            if src.shape[2] == 3:
                # 若源图像有三个通道, 则转化为灰度图
                graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
            elif src.shape == 1:
                graySrc = blurredSrc
        else:
            if src.shape[2] == 3:
                graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        # 边缘检测函数, 它会产生明显的边缘线条, 灰度图像更是如此
        cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)

        # 将 graySrc 作为输出图像
        return graySrc

    def strokeEdgesWhiteBg(self, src, blurKsize = 7, edgeKsize = 5):
        """ 将源图像背景变为白色, 并描绘出黑色的边缘 """

        # 若要关闭模糊效果, 可以将blurKsize的值设为3以下
        if blurKsize >= 3:
            blurredSrc = cv2.medianBlur(src, blurKsize)
            if src.shape[2] == 3:
                # 若源图像有三个通道, 则转化为灰度图
                graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
            elif src.shape == 1:
                graySrc = blurredSrc
        else:
            if src.shape[2] == 3:
                graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        # 边缘检测函数, 它会产生明显的边缘线条, 灰度图像更是如此
        cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)

        # 归一化系数, 将原来的 黑色背景、白色边缘图像 转换为 黑色边缘、白色背景图像
        normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)

        # 将 normalizedInverseAlpha 作为输出图像
        return np.array(normalizedInverseAlpha * 255, dtype = np.uint8)

    def canny(self, src, threshold1, threshold2, L2gradient = False):
        return cv2.Canny(src, threshold1, threshold2, L2gradient = L2gradient)

""" 模糊滤波器
 @extend VConvolutionFilter
 """
class BlurFilter(VConvolutionFilter):
    """ 2 像素半径的模糊滤波器 """

    def __init__(self):
        kernel = np.full((5, 5), 0.04)
        super(BlurFilter, self).__init__(kernel)

    def blur(self, src, ksize, dst = None, anchor = None, borderType = None):
        """
        blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst
            @brief 均值滤波, 这种滤波方法就是取一个像素的邻域内各像素的平均值作为滤波结果

            :param src 原始图像
            :param ksize 核（领域）大小, 以下例子邻域大小为 5 * 5
            :param dst 滤波后的图像
            :param anchor 邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
            :param borderType 是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT
        """
        cv2.blur(src, ksize, dst, anchor, borderType)

    def boxFilter(self, src, ddepth, ksize, dst = None, anchor = None, normalize = None, borderType = None):
        """
        boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) -> dst
            @brief 均值滤波：与 blur 函数相关的 boxFilter 函数

            :param src 原始图像
            :param ddepth 输出图像的深度(-1表示使用原始图像的深度)
            :param dst 滤波后的图像
            :param ksize 核（领域）大小, 以下例子邻域大小为 5 * 5
            :param anchor 邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
            :param normalize 等于 false 时相当于邻域内各像素的数值求和
                              等于 true 时，计算结果等效于 blur 函数
            :param borderType 是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT
        """
        cv2.boxFilter(src, ddepth, ksize, dst, anchor, normalize, borderType)

    def GaussianBlur(self, src, ksize, sigmaX, dst = None, sigmaY = None, borderType = None):
        """
        GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
            @brief 高斯滤波, 意义：
                    1. 均值滤波对邻域内各个像素采用统一的权值, 这种方式对大多数应用来说不是最佳的
                    2. 高斯滤波采取邻域内越靠近的值提供越大的权重的方式计算平均值, 权重的选取采用高斯函数的形式
                    3. 高斯函数有个非常好的特点, 就是无论在时域还是频域都是钟形的
                    4. 通过控制 borderType 可以控制低通滤波的截止频率

            :param src 原始图像
            :param ksize 核（领域）大小, 以下例子邻域大小为 5 * 5, 值越大模糊程度越大
            :param sigmaX 一般取 0
            :param dst 滤波后的图像
            :param sigmaY 通常情况下 sigmaY 取与 sigmaX 相同的值, 这时可以不写出来, 也就是用它的默认值 0
            :param borderType 高斯滤波的参数, 可用来控制低通滤波的截止滤波
        """
        cv2.GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType)

    def medianBlur(self, src, ksize, dst=None):
        """
        medianBlur(src, ksize[, dst]) -> dst
            @brief 中值滤波器, 是一种最常用的非线性滤波器, 它是取邻域内各点的统计中值作为输出的
                    1. 这种滤波器可以有效的去除椒盐噪声, 还能保持图像中各物体的边界不被模糊掉
                    2. 这种滤波器只能使用正方形的邻域

            :param src 原始图像
            :param ksize 核（领域）大小, 以下例子邻域大小为 5 * 5
            :param dst 滤波后的图像
        """
        cv2.medianBlur(src, ksize, dst)


""" 浮雕滤波器
 @extend VConvolutionFilter
 """
class EmbossFilter(VConvolutionFilter):
    """ 1 像素半径的浮雕滤波器, 同时具有模糊（正的权重）和锐化（负的权重）的作用, 会产生一种脊状或浮雕的效果 """

    def __init__(self):
        kernel = np.array([[-2, -1, 0],
                           [-1,  1, 1],
                           [ 0,  1, 2]])
        super(EmbossFilter, self).__init__(kernel)


""" 可分离滤波器 """
class sepFilter:
    """ 可分离滤波器 """

    def sepFilter2D(self, src, ddepth, kernelX, kernelY, dst = None, anchor = None, delta = None, borderType = None):
        """
        sepFilter2D(src, ddepth, kernelX, kernelY[, dst[, anchor[, delta[, borderType]]]]) -> dst
            @brief 可分离滤波器
                    一个 2 维滤波器, 若可分离为 x 和 y 方向两个独立的 1 维滤波器, 那么该 2 维滤波器就称为 可分离滤波器
                    高斯滤波器就是一个典型的可分离滤波器, 具有这种性质的滤波器有快速算法, 可比不具有这个性质的普通滤波器更高效地计算

            :param src 原始图像
            :param ddepth 输出图像的深度(-1表示使用原始图像的深度)
            :param kernelX x方向的核（领域）大小
            :param kernelY y方向的核（领域）大小
            :param dst 滤波后的图像
            :param anchor 邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
            :param delta 在将 过滤后的像素 存储在dst之前 添加可选值
            :param borderType 是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT
        """
        cv2.sepFilter2D(src, ddepth, kernelX, kernelY, dst, anchor, delta, borderType)
