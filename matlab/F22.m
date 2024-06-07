% 在此处设置数据文件路径
dataFilePath = '22.csv';
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
% 预测因变量
y_pred = a*x1.^2 + b*x2.^2 + c*x1.*x2 + d*x1 + e*x2 + f;
% 计算回归分析指标参数
SSE = sum((y - y_pred).^2);
MSE = SSE / length(y);
RMSE = sqrt(MSE);
MAE = mean(abs(y - y_pred));
R2 = 1 - SSE / sum((y - mean(y)).^2);
% 输出非线性回归方程和回归分析指标参数
fprintf('非线性回归方程：y = %.4f*x1^2 + %.4f*x2^2 + %.4f*x1*x2 + %.4f*x1 + %.4f*x2 + %.4f\n', a, b, c, d, e, f);
fprintf('回归分析指标参数：\n');
fprintf('SSE: %.4f\n', SSE);
fprintf('MSE : %.4f\n', MSE);
fprintf('RMSE: %.4f\n', RMSE);
fprintf('MAE : %.4f\n', MAE);
fprintf('R^2 : %.4f\n', R2);
% 绘制真实值和预测值的对比折线图
figure;
plot(y, 'b-', 'LineWidth', 2);
hold on;
plot(y_pred, 'r--', 'LineWidth', 2);
hold off;
legend('真实值', '预测值');
xlabel('样本序号');
ylabel('孔隙率');
title('真实值和预测值的对比');