# CRAFT
Text detection 

Hiểu về craft:
paper: https://arxiv.org/pdf/1904.01941.pdf

Về dữ liệu:
- Synthetic image với nhãn cấp độ ký tự. Chúng ta sẽ tạo heat map để biểu diễn ground truth label là region score (tỉ lệ 1 pixel có là tâm của một ký tự không) và affinity score (Tỷ lệ một ảnh là tâm của 2 ký tự liền kề). Có 3 bước để tạo heatmap: 1) Chuẩn bị 2-dimensional isotropic Gausian map; 2) Tính toán ma trận perspective transform giữa Gaussian map và mỗi box ký tự; 3) Dùng ma trận tìm được để chuyển Gaussian map về hình dạng của box ký tự. Đối với affinity score, ta sẽ vẽ các đường chéo nối các đỉnh đối diện nhau của box ký tự, tạo ra 2 tam giác upper và lower. Và một affinity box sẽ được tạo ra có đỉnh là là tâm của 4 cái tam giác của 2 box ký tự liền kề.
![alt text](https://github.com/chauthehan/CRAFT/blob/master/image/generate.png)


- Weakly-Supervised learning: không giống như synthetic datasets, ảnh thực chỉ có nhãn ở cấp độ từ. Mục tiêu của ta là tạo character box từ mỗi word box này. Khi có một ảnh thực, mô hình tạm thời (đang được train) sẽ dự đoán character region score của các từ đã được cắt ra để tạo ra character-level bouding boxes. Để thể hiện độ tin cậy về dự đoán của mô hình tạm thời,  giá trị của confidence map ở mỗi word box sẽ được tính dựa trên tỷ lệ của số lượng ký tự phát hiện được và số lượng ký tự thực tế, điều này sẽ được dùng để tính loss và cập nhật trọng số.  Các bước thực hiện: đầu tiên là cắt các word box ra, sau đó dùng model tạm thời để dự đoán region score (heat map), tiếp theo ta sẽ dùng thuật toán watershed để tách các ký tự ra để tạo ra character bounding box. Cuối cùng, tạo độ của các character box sẽ được chuyển lại về tạo độ trong ảnh thực. Pseudo-ground truths cho region score và affinity scỏe sẽ được tạo ra giống như ở bước trên.

![alt text](https://github.com/chauthehan/CRAFT/blob/master/image/training_stream.png)


Với phương pháp weakly-supervised learning, chúng ta phải train với các pseudo-GTs không hoàn hoản, tức là các nhãn bị sai, điều này dễ dẫn đến đầu ra character regions bị mờ. Để giải quyết điều này, chúng ta sẽ đo đạc chất lượng của pseudo-GTs sử dụng độ dài của mỗi từ ( vì mỗi từ sẽ có nhãn nên ta có thể biết được số ký tự trong từ đó). Với R(w) và l(w) là bounding box region và độ dài của từ của mẫu w. lc(w) là tổng số lượng character được dự đoán, thì độ tự tin Sconf(w) đưuọc tính dựa theo công thức: 

![alt text](https://github.com/chauthehan/CRAFT/blob/master/image/formula1.png)





![alt text](https://github.com/chauthehan/CRAFT/blob/master/image/generate.png)



