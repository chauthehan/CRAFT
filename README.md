# CRAFT
Text detection 

Hiểu về craft:
paper: https://arxiv.org/pdf/1904.01941.pdf

Về dữ liệu:
- Synthetic image với nhãn cấp độ ký tự. Chúng ta sẽ tạo heat map để biểu diễn ground truth label là region score (tỉ lệ 1 pixel có là tâm của một ký tự không) và affinity score (Tỷ lệ một ảnh là tâm của 2 ký tự liền kề). Có 3 bước để tạo heatmap: 1) Chuẩn bị 2-dimensional isotropic Gausian map; 2) Tính toán ma trận perspective transform giữa Gaussian map và mỗi box ký tự; 3) Dùng ma trận tìm được để chuyển Gaussian map về hình dạng của box ký tự. Đối với affinity score, ta sẽ vẽ các đường chéo nối các đỉnh đối diện nhau của box ký tự, tạo ra 2 tam giác upper và lower. Và một affinity box sẽ được tạo ra có đỉnh là là tâm của 4 cái tam giác của 2 box ký tự liền kề.

![alt text](https://github.com/chauthehan/CRAFT/blob/master/image/generate.png)



