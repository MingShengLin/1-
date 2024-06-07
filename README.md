# 基于回归模型的插层熔喷非织造材料的性能研究
整个课程设计完成主要用了两种编程语言，一开始是先用python进行编程的，后来在进行进一步做非线性回归分析时，因本人能力问题，耗费长时间，始终没能将一个完成的结果跑通，被迫将数据集重新手动分类并利用matlab进行编程，但好在最后的效果还不错。本次课设主要是对查找的初始数据集进行了一次相较简单的数据清洗，数据可视化。并利用数理统计的方法针对数据样本进行分析，分析插层后结构变量、产品性能的变化规律，并建立多项式非线性回归模型请研究工艺参数与结构变量之间的关系。

## 运行环境：
PyCharm社区版2022.3
MATLAB R2022b
 ## 插层后结构变量、产品性能的变化规律
![结构图](https://github.com/MingShengLin/1-/assets/138376786/d44dd2f4-f90a-4a47-b9e9-ed9a130979c8)

### 数据可视化与异常值处理
利用SPSSpro绘制折线图
![数据可视化](https://github.com/MingShengLin/1-/assets/138376786/ca9639ab-9270-4491-89aa-a6e746a9976d)
压缩回弹性率的盒须图
![盒须图](https://github.com/MingShengLin/1-/assets/138376786/70c5808c-9137-456c-937e-364e6beee1c0)
通过对同一组实验样本插层前后的实验数据差值按照插层率的大小排序进行正态分布检验

![过滤效率差（%）_distribution_fit](https://github.com/MingShengLin/1-/assets/138376786/6c71ef1e-1bff-43dc-922d-69cf73b030e0)
![过滤效率差](https://github.com/MingShengLin/1-/assets/138376786/2e4e5d13-5e8e-4095-a21e-8db73111500e)
![过滤阻力差Pa_distribution_fit](https://github.com/MingShengLin/1-/assets/138376786/050afbce-d5e6-4a30-b583-f5e0724d920c)
![厚度差mm_distribution_fit](https://github.com/MingShengLin/1-/assets/138376786/eaaf107c-474f-4c86-b6f7-419c2244e9d2)
![孔隙率差（%）_distribution_fit](https://github.com/MingShengLin/1-/assets/138376786/bc744571-e5db-4148-a339-63c6747afbb6)
![压缩回弹性率差（%）_distribution_fit](https://github.com/MingShengLin/1-/assets/138376786/bd73220c-ba45-4e28-982e-c9cb9265a154)
### 结论
可得到结构变量中厚度、孔隙率、压缩回弹性变化幅度于插层前后显著增大，产品性能中过滤阻力、过滤效率变化幅度于插层前后显著增大，产品性能中透气性插层前后变化幅度则属于中等程度
##数据归一化处理
正常来说进行数据分析都要进行归一化处理，但本数据用归一化处理后，建立的数学模型，效果比未归一化处理的模型效果差很多，所以并没有把归一化处理的结果放到当中来
## 工艺参数与结构变量之间的关系
### 模型建立
![image](https://github.com/MingShengLin/1-/assets/138376786/504461ab-d3f6-4662-89a9-709322d86111)
### 多项式非线性回归
![image](https://github.com/MingShengLin/1-/assets/138376786/fc1056b6-0128-4f03-9d4f-6a956c6b7eb6)
![image](https://github.com/MingShengLin/1-/assets/138376786/b563b1a5-a5c5-4b76-8d3f-d504921621ae)
### 最终模型
![image](https://github.com/MingShengLin/1-/assets/138376786/62f8f3af-9577-4686-ae53-88f6d4e86c40)

### 结论
从图像中可知接收距离增大时，通过插层熔喷技术得到的纤维粘合性较差，会导致纤网的蓬松性提升，纤维直径增大，孔隙率随之增大。

