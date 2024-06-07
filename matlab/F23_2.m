clc;clear
% 在此处设置数据文件路径
dataFilePath = '23.csv';
% 读取数据文件
data = csvread(dataFilePath);
% 提取自变量和因变量
x1 = data(:, 1);
x2 = data(:, 2);
y = data(:, 3);
% 构建非线性方程的矩阵形式
X = [x1.^2, x2.^2, x1.*x2, x1, x2, ones(size(x1))];
% 使用线性回归方法求解非线性模型的系数
coeffs = X\y;
% 提取系数
a = coeffs(1);
b = coeffs(2);
c = coeffs(3);
d = coeffs(4);
e = coeffs(5);
f = coeffs(6);
% 生成网格点
x1_range = linspace(min(x1), max(x1), 100);
x2_range = linspace(min(x2), max(x2), 100);
[x1_grid, x2_grid] = meshgrid(x1_range, x2_range);
% 计算预测值
y_pred = a*x1_grid.^2 + b*x2_grid.^2 + c*x1_grid.*x2_grid + d*x1_grid + e*x2_grid + f;
% 绘制三维曲面图
figure;
surf(x1_grid, x2_grid, y_pred);
xlabel('接收距离 x1');
ylabel('热空气速度 x2');
zlabel('压缩回弹性率 y');
title('非线性回归方程曲面图');