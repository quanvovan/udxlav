S-DCNet
- Cấu trúc chương trình bao gồm: 
(Nguồn tham khảo: https://github.com/xhp-hust-2018-2011/S-DCNet)
   + Folder ‘model’: chứa model đã được train sẵn
   + Folder ‘Network’: chứa các file cấu trúc mạng SDCNet (class_func.py, merge_func.py, SDCNet.py)
   + Folder ‘Test_Data’: chứa các tập dữ liệu để test
	o Sample_One: folder dùng để test ảnh bất kỳ
	o SH_partA_Density_map, SH_partB_Density_map: folder chứa tập dữ liệu ShanghaiTech
   + Iotools.py: write file .txt (log.txt)
   + load_data_V2.py: chuyển dữ liệu từ hình ảnh sang dataset của pytorch
   + main_process.py: phần xử lý chính
   + SHAB_main.py: dùng để test dữ liệu của bộ dataset ShanghaiTech
   + One Sample.py (tự thêm vào): dùng để test ảnh bất kỳ
   + LICENSE
   + Requirements.txt
   + README.TXT: hướng dẫn sử dụng + hướng dẫn cài đặt 

- Hướng dẫn cài đặt 
   + Ngôn ngữ lập trình Python 3.6
   + IDE khuyến nghị: PyCharm Community Edition
	Link tham khảo: https://www.jetbrains.com/pycharm/download/
   + Requirements
	+ python==3.6.2		+ pytorch>=0.4.0
	+ numpy==1.14.0		+ scikit-image==0.13.1
	+ scipy==1.0.0		+ pandas==0.22.0

- Hướng dẫn sử dụng
   + Để chạy test trên bộ dữ liệu ShanghaiTech: Run file SHAB_main.py
   + Để chạy test các ảnh khác chạy file One_Sample.py, 
	sau đó chọn ảnh cần test (tham khảo video hướng dẫn)
