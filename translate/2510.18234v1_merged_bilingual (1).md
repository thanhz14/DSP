# Bản dịch song ngữ

**English:** ============================================================
--- Page 1 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 1 ---  
============================================================

---

**English:** <|ref|>title<|/ref|><|det|>[[205, 132, 790, 157]]<|/det|>
# DeepSeek-OCR: Contexts Optical Compression  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[205, 132, 790, 157]]<|/det|>
# DeepSeek-OCR: Kỹ thuật nén dữ liệu quang học dựa trên ngữ cảnh

---

**English:** <|ref|>text<|/ref|><|det|>[[350, 187, 646, 203]]<|/det|>
Haoran Wei, Yaofeng Sun, Yukun Li  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[350, 187, 646, 203]]<|/det|>  
Haoran Wei, Yaofeng Sun, Yukun Li

---

**English:** <|ref|>text<|/ref|><|det|>[[444, 215, 551, 230]]<|/det|>
DeepSeek- AI  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[444, 215, 551, 230]]<|/det|>
DeepSeek – Trí tuệ nhân tạo

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[450, 263, 547, 283]]<|/det|>
## Abstract  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[450, 263, 547, 283]]<|/det|>
## Tóm tắt

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 306, 883, 564]]<|/det|>
We present DeepSeek- OCR as an initial investigation into the feasibility of compressing long contexts via optical 2D mapping. DeepSeek- OCR consists of two components: DeepEncoder and DeepSeek3B- MoE- A570M as the decoder. Specifically, DeepEncoder serves as the core engine, designed to maintain low activations under high- resolution input while achieving high compression ratios to ensure an optimal and manageable number of vision tokens. Experiments show that when the number of text tokens is within 10 times that of vision tokens (i.e., a compression ratio \(< 10\times\) ), the model can achieve decoding (OCR) precision of \(97\%\) . Even at a compression ratio of \(20\times\) , the OCR accuracy still remains at about \(60\%\) . This shows considerable promise for research areas such as historical long- context compression and memory forgetting mechanisms in LLMs. Beyond this, DeepSeek- OCR also demonstrates high practical value. On OmniDocBench, it surpasses GOT- OCR2.0 (256 tokens/page) using only 100 vision tokens, and outperforms MinerU2.0 (6000+ tokens per page on average) while utilizing fewer than 800 vision tokens. In production, DeepSeek- OCR can generate training data for LLMs/VLMs at a scale of \(200k+\) pages per day (a single A100- 40G). Codes and model weights are publicly accessible at http://github.com/deepseek- ai/DeepSeek- OCR.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 306, 883, 564]]<|/det|>
We present DeepSeek- OCR as an initial investigation into the feasibility of compressing long contexts via optical 2D mapping. DeepSeek- OCR consists of two components: DeepEncoder and DeepSeek3B- MoE- A570M as the decoder. Specifically, DeepEncoder serves as the core engine, designed to maintain low activations under high- resolution input while achieving high compression ratios to ensure an optimal and manageable number of vision tokens. Experiments show that when the number of text tokens is within 10 times that of vision tokens (i.e., a compression ratio \(< 10\times\) ), the model can achieve decoding (OCR) precision of \(97\%\). Even at a compression ratio of \(20\times\), the OCR accuracy still remains at about \(60\%\). This shows considerable promise for research areas such as historical long- context compression and memory forgetting mechanisms in LLMs. Beyond this, DeepSeek- OCR also demonstrates high practical value. On OmniDocBench, it surpasses GOT- OCR2.0 (256 tokens/page) using only 100 vision tokens, and outperforms MinerU2.0 (6000+ tokens per page on average) while utilizing fewer than 800 vision tokens. In production, DeepSeek- OCR can generate training data for LLMs/VLMs at a scale of \(200k+\) pages per day (a single A100- 40G). Codes and model weights are publicly accessible at http://github.com/deepseek- ai/DeepSeek- OCR.<|ref|>text<|/ref|><|det|>[[115, 306, 883, 564]]<|/det|>  
Chúng tôi giới thiệu DeepSeek-OCR như một nghiên cứu sơ bộ về khả năng nén các đoạn văn dài thông qua phương pháp lập bản đồ 2D quang học. DeepSeek-OCR bao gồm hai thành phần chính: DeepEncoder và DeepSeek3B-MoE-A570M, trong đó DeepEncoder đóng vai trò là bộ phận xử lý chính; nó được thiết kế để duy trì mức độ hoạt động thấp ngay cả với các dữ liệu đầu vào có độ phân giải cao, đồng thời đạt được tỷ lệ nén cao nhằm đảm bảo số lượng các “token” hình ảnh được sử dụng là vừa phải và dễ quản lý. Các thí nghiệm cho thấy khi số lượng token văn bản chỉ bằng khoảng 1/10 so với số lượng token hình ảnh (tức tỷ lệ nén < 10 lần), mô hình vẫn có thể đạt độ chính xác trong việc giải mã văn bản lên đến 97%. Ngay cả ở tỷ lệ nén 20 lần, độ chính xác vẫn khoảng 60%. Điều này mở ra nhiều tiềm năng cho các lĩnh vực nghiên cứu như việc nén các đoạn văn dài có tính lịch sử hoặc cơ chế “quên lãng” thông tin trong các mô hình LLM. Ngoài ra, DeepSeek-OCR còn thể hiện giá trị thực tiễn cao: trên nền tảng OmniDocBench, nó vượt trội hơn so với GOT-OCR2.0 (sử dụng 256 token/trang) khi chỉ cần 100 token hình ảnh; đồng thời cũng vượt trội hơn MinerU2.0 (trung bình sử dụng hơn 6000 token/trang) mà vẫn chỉ tiêu thụ chưa đầy 800 token hình ảnh. Trong thực tế ứng dụng, DeepSeek-OCR có thể tạo ra lượng dữ liệu huấn luyện lớn cho các mô hình LLM/VLM, với tốc độ lên đến hơn 200.000 trang mỗi ngày (sử dụng một card GPU loại A100-40G). Mã nguồn và thông tin về cấu hình mô hình có thể được tìm thấy tại địa chỉ http://github.com/deepseek-ai/DeepSeek-OCR.

---

**English:** ![Image 0_0](images/page_1_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 827, 881, 892]]<|/det|>
<center>Figure 1 | Figure (a) shows the compression ratio (number of text tokens in ground truth/number of vision tokens model used) testing on Fox [21] benchmark; Figure (b) shows performance comparisons on OmniDocBench [27]. DeepSeek-OCR can achieve state-of-the-art performance among end-to-end models enjoying the fewest vision tokens. </center>

**Tiếng Việt:** ![Hình 0_0](images/page_1_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 827, 881, 892]]<|/thông tin chi tiết|>
<center>Hình 1: Hình (a) thể hiện tỷ lệ nén (số lượng các ký hiệu văn bản so với số lượng các ký hiệu hình ảnh được mô hình sử dụng) khi thử nghiệm trên bài kiểm thử Fox [21]; Hình (b) so sánh hiệu suất của mô hình DeepSeek-OCR trên nền tảng OmniDocBench [27]. DeepSeek-OCR đạt được mức hiệu suất hàng đầu trong số các mô hình end-to-end, trong khi chỉ sử dụng số lượng ký hiệu hình ảnh tối thiểu.</center>

---

**English:** 
============================================================
--- Page 2 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 2 ---  
============================================================

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 99, 210, 117]]<|/det|>
## Contents  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 99, 210, 117]]<|/det|>
## Nội dung

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 140, 884, 158]]<|/det|>
1 Introduction 3  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 140, 884, 158]]<|/det|>  
1. Giới thiệu 3

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 175, 884, 193]]<|/det|>
2 Related Works 4  

**Tiếng Việt:** <|ref|>văn bản<|/ref|><|det|>[[115, 175, 884, 193]]<|/det|>
2 Các tác phẩm liên quan 4

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 199, 884, 216]]<|/det|>
2.1 Typical Vision Encoders in VLMs 4  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 199, 884, 216]]<|/det|>
2.1 Các bộ mã hóa hình ảnh điển hình trong các mô hình nhận diện hình ảnh ảo 4

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 222, 884, 239]]<|/det|>
2.2 End-to-end OCR Models 4  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 222, 884, 239]]<|/det|>
2.2 Các mô hình OCR hoạt động theo nguyên lý từ đầu đến cuối 4

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 257, 884, 275]]<|/det|>
3 Methodology 5  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 257, 884, 275]]<|/det|>  
3 Phương pháp luận 5

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 280, 884, 297]]<|/det|>
3.1 Architecture 5  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 280, 884, 297]]<|/det|>
3.1 Kiến trúc 5

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 303, 884, 320]]<|/det|>
3.2 DeepEncoder 5  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 303, 884, 320]]<|/det|>
3.2 DeepEncoder 5

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 326, 884, 343]]<|/det|>
3.2.1 Architecture of DeepEncoder 5  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 326, 884, 343]]<|/det|>
3.2.1 Cấu trúc của DeepEncoder 5

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 349, 884, 366]]<|/det|>
3.2.2 Multiple resolution support 6  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 349, 884, 366]]<|/det|>
3.2.2 Hỗ trợ nhiều độ phân giải khác nhau 6

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 371, 884, 389]]<|/det|>
3.3 The MoE Decoder 7  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 371, 884, 389]]<|/det|>
3.3 Bộ giải mã MoE 7

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 394, 884, 411]]<|/det|>
3.4 Data Engine 7  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 394, 884, 411]]<|/det|>
3.4 Máy chạy dữ liệu 7

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 417, 884, 433]]<|/det|>
3.4.1 OCR 1.0 data 7  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 417, 884, 433]]<|/det|>
3.4.1 Dữ liệu OCR 1.0 7

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 440, 884, 456]]<|/det|>
3.4.2 OCR 2.0 data 8  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 440, 884, 456]]<|/det|>  
Dữ liệu OCR 2.0 phiên bản 8

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 462, 884, 479]]<|/det|>
3.4.3 General vision data 9  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 462, 884, 479]]<|/det|>
3.4.3 Dữ liệu thị giác tổng quát 9

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 485, 884, 501]]<|/det|>
3.4.4 Text-only data 9  

**Tiếng Việt:** <|ref|>văn bản<|/ref|><|det|>[[180, 485, 884, 501]]<|/det|>
3.4.4 Dữ liệu chỉ chứa văn bản 9

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 506, 884, 524]]<|/det|>
3.5 Training Pipelines 9  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 506, 884, 524]]<|/det|>
3.5 Quy trình đào tạo 9

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 529, 884, 546]]<|/det|>
3.5.1 Training DeepEncoder 10  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 529, 884, 546]]<|/det|>
3.5.1 Đào tạo mô hình DeepEncoder 10

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 551, 884, 568]]<|/det|>
3.5.2 Training DeepSeek- OCR 10  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 551, 884, 568]]<|/det|>
3.5.2 Đào tạo mô hình DeepSeek-OCR 10

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 586, 884, 603]]<|/det|>
4 Evaluation 10  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 586, 884, 603]]<|/det|>
4 Đánh giá 10

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 609, 884, 626]]<|/det|>
4.1 Vision- text Compression Study 10  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 609, 884, 626]]<|/det|>
4.1 Nghiên cứu về việc nén dữ liệu văn bản dựa trên công nghệ thị giác 10

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 632, 884, 649]]<|/det|>
4.2 OCR Practical Performance 12  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 632, 884, 649]]<|/det|>
4.2 Hiệu suất thực tế của công nghệ OCR 12

---

**English:** <|ref|>text<|/ref|><|det|>[[140, 655, 884, 672]]<|/det|>
4.3 Qualitative Study 12  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[140, 655, 884, 672]]<|/det|>
4.3 Nghiên cứu định tính 12

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 678, 884, 694]]<|/det|>
4.3.1 Deep parsing 12  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 678, 884, 694]]<|/det|>
4.3.1 Phân tích sâu 12

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 700, 884, 717]]<|/det|>
4.3.2 Multilingual recognition 16  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 700, 884, 717]]<|/det|>
4.3.2 Nhận dạng ngôn ngữ đa dạng 16

---

**English:** <|ref|>text<|/ref|><|det|>[[180, 722, 884, 739]]<|/det|>
4.3.3 General vision understanding 17  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[180, 722, 884, 739]]<|/det|>
4.3.3 Khả năng hiểu biết tổng quát về hình ảnh 17

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 757, 884, 774]]<|/det|>
5 Discussion 18  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 757, 884, 774]]<|/det|>  
5. Thảo luận 18

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 792, 884, 810]]<|/det|>
6 Conclusion 19

**Tiếng Việt:** <|ref|>văn bản<|/ref|><|det|>[[115, 792, 884, 810]]<|/det|>  
6. Kết luận 19

---

**English:** 
============================================================
--- Page 3 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 3 ---  
============================================================

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 99, 270, 116]]<|/det|>
## 1. Introduction  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 99, 270, 116]]<|/det|>
## 1. Giới thiệu

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 130, 882, 227]]<|/det|>
Current Large Language Models (LLMs) face significant computational challenges when processing long textual content due to quadratic scaling with sequence length. We explore a potential solution: leveraging visual modality as an efficient compression medium for textual information. A single image containing document text can represent rich information using substantially fewer tokens than the equivalent digital text, suggesting that optical compression through vision tokens could achieve much higher compression ratios.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 130, 882, 227]]<|/det|>  
Các mô hình ngôn ngữ lớn hiện nay đối mặt với những thách thức lớn về mặt tính toán khi xử lý các nội dung văn bản dài, do mức độ tốn tài nguyên tăng theo cấp số nhân theo độ dài chuỗi văn bản. Chúng tôi đề xuất một giải pháp tiềm năng: tận dụng hình thức biểu đạt thông tin qua hình ảnh như một phương tiện nén hiệu quả cho dữ liệu văn bản. Một hình ảnh duy nhất chứa nội dung văn bản có thể truyền tải được nhiều thông tin hơn đáng kể so với việc sử dụng văn bản kỹ thuật số tương đương; điều này cho thấy rằng phương pháp nén thông tin thông qua hình ảnh có thể mang lại tỷ lệ nén cao hơn nhiều.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 235, 882, 331]]<|/det|>
This insight motivates us to reexamine vision- language models (VLMs) from an LLM- centric perspective, focusing on how vision encoders can enhance LLMs' efficiency in processing textual information rather than basic VQA [12, 16, 24, 32, 41] what humans excel at. OCR tasks, as an intermediate modality bridging vision and language, provide an ideal testbed for this vision- text compression paradigm, as they establish a natural compression- decompression mapping between visual and textual representations while offering quantitative evaluation metrics.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 235, 882, 331]]<|/det|>  
Nhận thức này thúc đẩy chúng ta xem xét lại các mô hình học máy thị giác-ngôn ngữ (Vision-Language Models – VLMs) từ góc độ tập trung vào các mô hình LLM, với trọng tâm là tìm hiểu cách các công cụ mã hóa thông tin thị giác có thể nâng cao hiệu quả xử lý dữ liệu văn bản của các mô hình LLM, thay vì chỉ tập trung vào những khả năng mà con người giỏi nhất, chẳng hạn như việc trả lời các câu hỏi đối thoại [12, 16, 24, 32, 41]. Các nhiệm vụ OCR, với vai trò là phương tiện kết nối giữa thị giác và ngôn ngữ, tạo điều kiện lý tưởng để kiểm thử mô hình này; chúng thiết lập mối quan hệ giữa quá trình nén và giải nén dữ liệu thị giác với dữ liệu văn bản một cách tự nhiên, đồng thời cung cấp các chỉ số đánh giá định lượng cần thiết.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 339, 880, 372]]<|/det|>
Accordingly, we present DeepSeek- OCR, a VLM designed as a preliminary proof- of- concept for efficient vision- text compression. Our work makes three primary contributions:  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 339, 880, 372]]<|/det|>  
Theo đó, chúng tôi giới thiệu DeepSeek-OCR – một hệ thống VLM được thiết kế như một bằng chứng sơ bộ về khả năng nén dữ liệu hình ảnh kết hợp văn bản một cách hiệu quả. Công trình của chúng tôi đóng góp ba điểm chính:

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 379, 882, 509]]<|/det|>
First, we provide comprehensive quantitative analysis of vision- text token compression ratios. Our method achieves \(96\% +\) OCR decoding precision at \(9 - 10\times\) text compression, \(\sim 90\%\) at \(10 - 12\times\) compression, and \(\sim 60\%\) at \(20\times\) compression on Fox [21] benchmarks featuring diverse document layouts (with actual accuracy being even higher when accounting for formatting differences between output and ground truth), as shown in Figure 1(a). The results demonstrate that compact language models can effectively learn to decode compressed visual representations, suggesting that larger LLMs could readily acquire similar capabilities through appropriate pretraining design.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 379, 882, 509]]<|/det|>  
Trước hết, chúng tôi tiến hành phân tích định lượng toàn diện về tỷ lệ nén các đối tượng hình ảnh và văn bản. Phương pháp của chúng tôi đạt độ chính xác khi giải mã dữ liệu nén lên đến \(96\%\) ở mức độ nén \(9 – 10\times\); độ chính xác này giảm xuống khoảng \(90\%\) ở mức độ nén \(10 – 12\times\), và chỉ còn khoảng \(60\%\) ở mức độ nén \(20\times\), được thể hiện trên bài kiểm thử Fox [21] với nhiều loại cấu trúc văn bản khác nhau. Độ chính xác thực tế còn cao hơn nữa nếu xét đến sự khác biệt về định dạng giữa dữ liệu đầu ra và dữ liệu chuẩn, như được minh họa trong Hình 1(a). Kết quả này cho thấy các mô hình ngôn ngữ có kích thước nhỏ vẫn có thể học cách giải mã các dữ liệu hình ảnh đã được nén một cách hiệu quả; điều này gợi ý rằng các mô hình ngôn ngữ lớn hơn cũng hoàn toàn có thể đạt được khả năng tương tự nếu được thiết kế quá trình huấn luyện phù hợp.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 515, 882, 612]]<|/det|>
Second, we introduce DeepEncoder, a novel architecture that maintains low activation memory and minimal vision tokens even with high- resolution inputs. It serially connects window attention and global attention encoder components through a \(16\times\) convolutional compressor. This design ensures that the window attention component processes a large number of vision tokens, while the compressor reduces vision tokens before they enter the dense global attention component, achieving effective memory and token compression.  

**Tiếng Việt:** Thứ hai, chúng tôi giới thiệu DeepEncoder – một kiến trúc mới mẻ giúp giảm thiểu lượng bộ nhớ cần sử dụng và số lượng các thông tin đầu vào liên quan đến hình ảnh, ngay cả với những dữ liệu có độ phân giải cao. Cấu trúc này kết nối các thành phần xử lý thông tin hình ảnh theo thứ tự: thành phần xử lý thông tin theo từng khu vực nhỏ và thành phần xử lý thông tin toàn diện, thông qua một bộ thu nhỏ dữ liệu có kích thước \(16\times\). Thiết kế này đảm bảo rằng thành phần xử lý thông tin theo từng khu vực nhỏ có thể xử lý một lượng lớn dữ liệu hình ảnh, trong khi bộ thu nhỏ này giúp giảm bớt số lượng thông tin đó trước khi chúng được chuyển đến thành phần xử lý toàn diện, từ đó nâng cao hiệu quả sử dụng bộ nhớ và giảm thiểu lượng dữ liệu cần xử lý.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 619, 882, 718]]<|/det|>
Third, we develop DeepSeek- OCR based on DeepEncoder and DeepSeek3B- MoE [19, 20]. As shown in Figure 1(b), it achieves state- of- the- art performance within end- to- end models on OmniDocBench while using the fewest vision tokens. Additionally, we equip the model with capabilities for parsing charts, chemical formulas, simple geometric figures, and natural images to enhance its practical utility further. In production, DeepSeek- OCR can generate 33 million pages of data per day for LLMs or VLMs using 20 nodes (each with 8 A100- 40G GPUs).  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 619, 882, 718]]<|/det|>  
Thứ ba, chúng tôi đã phát triển công cụ DeepSeek-OCR dựa trên các mô hình DeepEncoder và DeepSeek3B-MoE [19, 20]. Như được minh họa trong Hình 1(b), công cụ này đạt được hiệu suất hàng đầu trong số các mô hình end-to-end trên bộ dữ liệu OmniDocBench, trong khi chỉ sử dụng một lượng nhỏ các yếu tố liên quan đến xử lý hình ảnh. Ngoài ra, chúng tôi còn trang bị cho mô hình này khả năng phân tích các biểu đồ, công thức hóa học, hình dạng hình học đơn giản và hình ảnh tự nhiên, nhằm nâng cao tính ứng dụng thực tiễn của nó. Trong thực tế, với 20 node mỗi node được trang bị 8 GPU loại A100-40G, DeepSeek-OCR có thể tạo ra 33 triệu trang dữ liệu mỗi ngày để phục vụ các mô hình LLM hoặc VLM.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 725, 882, 886]]<|/det|>
In summary, this work presents a preliminary exploration of using visual modality as an efficient compression medium for textual information processing in LLMs. Through DeepSeek- OCR, we demonstrate that vision- text compression can achieve significant token reduction (7- 20x) for different historical context stages, offering a promising direction for addressing long- context challenges in large language models. Our quantitative analysis provides empirical guidelines for VLM token allocation optimization, while the proposed DeepEncoder architecture showcases practical feasibility with real- world deployment capabilities. Although focused on OCR as a proof- of- concept, this paradigm opens new possibilities for rethinking how vision and language modalities can be synergistically combined to enhance computational efficiency in large- scale text processing and agent systems.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 725, 882, 886]]<|/det|>  
Tóm lại, nghiên cứu này đề xuất một phương pháp tiếp cận sơ bộ trong việc sử dụng các công nghệ xử lý hình ảnh như một phương tiện nén hiệu quả để xử lý thông tin văn bản trong các mô hình ngôn ngữ lớn. Thông qua công cụ DeepSeek-OCR, chúng tôi đã chứng minh rằng việc kết hợp công nghệ xử lý hình ảnh và văn bản có thể giúp giảm số lượng các ký hiệu được sử dụng trong quá trình xử lý đáng kể (từ 7 đến 20 lần), từ đó mở ra hướng đi mới để giải quyết những thách thức liên quan đến việc xử lý thông tin có ngữ cảnh dài trong các mô hình ngôn ngữ lớn. Phân tích định lượng của chúng tôi cung cấp những hướng dẫn thực tiễn cho việc tối ưu hóa cách phân bổ các ký hiệu trong các mô hình này, trong khi kiến trúc DeepEncoder được đề xuất đã chứng tỏ tính khả thi thực tế của phương pháp này thông qua các ứng dụng thực tế. Mặc dù nghiên cứu này tập trung vào công nghệ OCR như một ví dụ minh họa ý tưởng, nhưng nó mở ra nhiều khả năng mới để xem xét cách kết hợp hiệu quả giữa các công nghệ xử lý hình ảnh và ngôn ngữ, nhằm nâng cao hiệu suất tính toán trong các quá trình xử lý văn bản quy mô lớn cũng như các hệ thống tự động hóa.

---

**English:** 
============================================================
--- Page 4 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 4 ---
============================================================

---

**English:** ![Image 0_0](images/page_4_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 234, 880, 268]]<|/det|>
<center>Figure 2 | Typical vision encoders in popular VLMs. Here are three types of encoders commonly used in current open-source VLMs, all of which suffer from their respective deficiencies. </center>  

**Tiếng Việt:** ![Hình 0_0](images/page_4_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 234, 880, 268]]<|/thông tin chi tiết|>
<center>Hình 2 | Các bộ mã hóa hình ảnh phổ biến trong các hệ thống quản lý dữ liệu hình ảnh mở nguồn hiện nay. Dưới đây là ba loại bộ mã hóa thường được sử dụng; tất cả chúng đều có những hạn chế riêng.</center>

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 290, 291, 308]]<|/det|>
## 2. Related Works  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 290, 291, 308]]<|/det|>
## 2. Các công trình liên quan

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 323, 436, 340]]<|/det|>
### 2.1. Typical Vision Encoders in VLMs  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 323, 436, 340]]<|/det|>
### 2.1. Các bộ mã hóa hình ảnh điển hình trong các mô hình nhận diện hình ảnh ảo</td>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 350, 882, 624]]<|/det|>
Current open- source VLMs employ three main types of vision encoders, as illustrated in Figure 2. The first type is a dual- tower architecture represented by Vary [36], which utilizes parallel SAM [17] encoder to increase visual vocabulary parameters for high- resolution image processing. While offering controllable parameters and activation memory, this approach suffers from significant drawbacks: it requires dual image preprocessing that complicates deployment and makes encoder pipeline parallelism challenging during training. The second type is tile- based method exemplified by InternVL2.0 [8], which processes images by dividing them into small tiles for parallel computation, reducing activation memory under high- resolution settings. Although capable of handling extremely high resolutions, this approach has notable limitations due to its typically low native encoder resolution (below \(512 \times 512\) ), causing large images to be excessively fragmented and resulting in numerous vision tokens. The third type is adaptive resolution encoding represented by Qwen2- VL [35], which adopts the NaViT [10] paradigm to directly process full images through patch- based segmentation without tile parallelization. While this encoder can handle diverse resolutions flexibly, it faces substantial challenges with large images due to massive activation memory consumption that can cause GPU memory overflow, and sequence packing requires extremely long sequence lengths during training. Long vision tokens will slow down both prefill and generation phases of inference.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 350, 882, 624]]<|/det|>  
Các công cụ xử lý hình ảnh mã nguồn mở hiện nay sử dụng ba loại bộ mã hóa hình ảnh chính, như được minh họa trong Hình 2. Loại thứ nhất là kiến trúc gồm hai “tháp” xử lý, điển hình là công cụ Vary [36]; phương pháp này sử dụng các bộ mã hóa SAM [17] để tăng số lượng tham số cần thiết cho việc xử lý hình ảnh độ phân giải cao. Mặc dù cho phép điều chỉnh các tham số và sử dụng bộ nhớ kích hoạt, phương pháp này lại gặp phải nhiều hạn chế: quá trình xử lý hình ảnh trước cần phức tạp hơn, làm tăng độ khó trong việc triển khai và khó tận dụng tính song song của các luồng xử lý trong quá trình huấn luyện. Loại thứ hai là phương pháp dựa trên việc chia hình ảnh thành các ô nhỏ để xử lý song song, điển hình là công cụ InternVL2.0 [8]; phương pháp này giúp giảm lượng bộ nhớ cần thiết khi xử lý hình ảnh độ phân giải cao. Tuy có khả năng xử lý các hình ảnh độ phân giải rất cao, nhưng phương pháp này vẫn bị hạn chế do độ phân giải của các bộ mã hóa thường khá thấp (dưới 512 × 512), khiến việc xử lý các hình ảnh lớn trở nên phức tạp hơn. Loại thứ ba là phương pháp mã hóa với độ phân giải tự động điều chỉnh, điển hình là công cụ Qwen2-VL [35]; phương pháp này áp dụng công nghệ NaViT [10] để xử lý trực tiếp toàn bộ hình ảnh mà không cần chia chúng thành các ô nhỏ. Mặc dù có khả năng thích ứng với nhiều độ phân giải khác nhau, phương pháp này vẫn gặp nhiều khó khăn khi xử lý các hình ảnh lớn do lượng bộ nhớ cần thiết quá lớn, có thể dẫn đến tình trạng quá tải bộ nhớ GPU; đồng thời, quá trình huấn luyện cũng đòi hỏi các chuỗi dữ liệu có độ dài rất lớn. Những yếu tố này khiến việc xử lý hình ảnh trở nên chậm chạp hơn.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 647, 362, 663]]<|/det|>
### 2.2. End-to-end OCR Models  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 647, 362, 663]]<|/det|>
### 2.2. Các mô hình OCR hoạt động theo nguyên lý từ đầu đến cuối

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 673, 882, 899]]<|/det|>
OCR, particularly document parsing task, has been a highly active topic in the image- to- text domain. With the advancement of VLMs, a large number of end- to- end OCR models have emerged, fundamentally transforming the traditional pipeline architecture (which required separate detection and recognition expert models) by simplifying OCR systems. Nougat [6] first employs end- to- end framework for academic paper OCR on arXiv, demonstrating the potential of models in handling dense perception tasks. GOT- OCR2.0 [38] expands the scope of OCR2.0 to include more synthetic image parsing tasks and designs an OCR model with performance- efficiency trade- offs, further highlighting the potential of end- to- end OCR researches. Additionally, general vision models such as Qwen- VL series [35], InternVL series [8], and many their derivatives continuously enhance their document OCR capabilities to explore dense visual perception boundaries. However, a crucial research question that current models have not addressed is: for a document containing 1000 words, how many vision tokens are at least needed for decoding? This question holds significant importance for research in the principle that "a picture is worth a thousand words."

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 673, 882, 899]]<|/det|>  
Việc nhận dạng văn bản từ hình ảnh, đặc biệt là các công việc phân tích nội dung tài liệu, luôn là một lĩnh vực được quan tâm sâu rộng trong lĩnh vực chuyển đổi hình ảnh thành văn bản. Với sự phát triển của các mô hình trí tuệ nhân tạo, ngày càng nhiều mô hình OCR hoạt động theo nguyên lý “từ đầu đến cuối” đã xuất hiện, thay đổi căn bản cấu trúc truyền thống (vốn yêu cầu sử dụng các mô hình riêng biệt để phát hiện và nhận diện thông tin) bằng cách đơn giản hóa quy trình xử lý. Nougat [6] là người đầu tiên áp dụng cấu trúc này cho việc nhận dạng văn bản trong các bài báo khoa học trên arXiv, chứng minh tiềm năng của các mô hình này trong việc xử lý các nhiệm vụ phức tạp liên quan đến nhận thức hình ảnh. GOT-OCR2.0 [38] mở rộng phạm vi ứng dụng của OCR2.0 sang nhiều loại tác vụ phân tích hình ảnh hơn, đồng thời thiết kế các mô hình OCR với sự cân bằng giữa hiệu suất và tính hiệu quả, từ đó làm nổi bật thêm tiềm năng của các nghiên cứu về OCR theo nguyên lý “từ đầu đến cuối”. Ngoài ra, các mô hình nhận thức hình ảnh tổng quát như loạt Qwen-VL [35], InternVL [8] và nhiều phiên bản phái sinh của chúng cũng liên tục được cải thiện về khả năng nhận dạng văn bản từ hình ảnh, giúp mở rộng giới hạn của các công nghệ này. Tuy nhiên, vẫn còn một câu hỏi quan trọng mà các mô hình hiện tại chưa giải đáp được: Đối với một tài liệu gồm 1000 từ, ít nhất cần bao nhiêu thông tin hình ảnh là đủ để thực hiện quá trình nhận dạng văn bản? Câu hỏi này có ý nghĩa quan trọng đối với các nghiên cứu liên quan đến nguyên tắc “Một hình ảnh giá trị bằng ngàn lời nói”.

---

**English:** 
============================================================
--- Page 5 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 5 ---
============================================================

---

**English:** ![Image 0_0](images/page_5_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 260, 881, 327]]<|/det|>
<center>Figure 3 | The architecture of DeepSeek-OCR. DeepSeek-OCR consists of a DeepEncoder and a DeepSeek-3B-MoE decoder. DeepEncoder is the core of DeepSeek-OCR, comprising three components: a SAM [17] for perception dominated by window attention, a CLIP [29] for knowledge with dense global attention, and a \(16\times\) token compressor that bridges between them. </center>  

**Tiếng Việt:** ![Hình 0_0](images/page_5_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 260, 881, 327]]<|/thông tin chi tiết|>
<center>Hình 3 | Cấu trúc của DeepSeek-OCR. DeepSeek-OCR bao gồm một bộ mã hóa sâu (DeepEncoder) và một bộ giải mã sâu DeepSeek-3B-MoE. DeepEncoder là thành phần cốt lõi của DeepSeek-OCR, bao gồm ba thành phần chính: công cụ SAM [17] dùng để thu thập thông tin dựa trên cơ chế chú ý theo khung cửa sổ; công cụ CLIP [29] dùng để tích hợp kiến thức từ các nguồn khác nhau thông qua cơ chế chú ý toàn diện; và một bộ nén dữ liệu có kích thước \(16\times\) token, đóng vai trò kết nối các thành phần này lại với nhau.</center>

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[116, 350, 279, 368]]<|/det|>
## 3. Methodology  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[116, 350, 279, 368]]<|/det|>
## 3. Phương pháp tiếp cận</td>

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[116, 382, 259, 398]]<|/det|>
### 3.1. Architecture  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[116, 382, 259, 398]]<|/det|>
### 3.1. Kiến trúc</td>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 408, 882, 540]]<|/det|>
As shown in Figure 3, DeepSeek- OCR enjoys a unified end- to- end VLM architecture consisting of an encoder and a decoder. The encoder (namely DeepEncoder) is responsible for extracting image features and tokenizing as well as compressing visual representations. The decoder is used for generating the required result based on image tokens and prompts. DeepEncoder is approximately 380M in parameters, mainly composed of an 80M SAM- base [17] and a 300M CLIP- large [29] connected in series. The decoder adopts a 3B MoE [19, 20] architecture with 570M activated parameters. In the following paragraphs, we will delve into the model components, data engineering, and training skills.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 408, 882, 540]]<|/det|>  
Như được minh họa trong Hình 3, DeepSeek-OCR sử dụng một kiến trúc VLM tích hợp từ đầu đến cuối, bao gồm cả bộ mã hóa và bộ giải mã. Bộ mã hóa (tên là DeepEncoder) có nhiệm vụ trích xuất các đặc điểm hình ảnh, chuyển đổi chúng thành dạng “token” và sau đó nén chúng lại. Bộ giải mã được sử dụng để tạo ra kết quả mong muốn dựa trên các “token” hình ảnh và các thông tin hướng dẫn được cung cấp. DeepEncoder chứa khoảng 380 triệu tham số, được cấu tạo chủ yếu từ mô-đun SAM có dung lượng 80 triệu tham số [17] và mô-đun CLIP có dung lượng 300 triệu tham số [29], được kết nối liên tiếp với nhau. Bộ giải mã sử dụng kiến trúc MoE có 3 tỷ tham số hoạt động [19, 20], với tổng số 570 triệu tham số được sử dụng trong quá trình xử lý dữ liệu. Trong các phần tiếp theo, chúng ta sẽ tìm hiểu chi tiết hơn về các thành phần cấu tạo của mô hình này, quy trình xử lý dữ liệu và các kỹ thuật huấn luyện mô hình.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[116, 562, 267, 578]]<|/det|>
### 3.2. DeepEncoder  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[116, 562, 267, 578]]<|/det|>
### 3.2. DeepEncoder

---

**English:** <|ref|>text<|/ref|><|det|>[[116, 588, 882, 668]]<|/det|>
To explore the feasibility of contexts optical compression, we need a vision encoder with the following features: 1. Capable of processing high resolutions; 2. Low activation at high resolutions; 3. Few vision tokens; 4. Support for multiple resolution inputs; 5. Moderate parameter count. However, as described in the Section 2.1, current open- source encoders cannot fully satisfy all these conditions. Therefore, we design a novel vision encoder ourselves, named DeepEncoder.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[116, 588, 882, 668]]<|/det|>  
Để nghiên cứu khả năng áp dụng phương pháp nén dữ liệu hình ảnh dựa trên ngữ cảnh, chúng ta cần một bộ mã hóa hình ảnh có những đặc điểm sau: 1. Có khả năng xử lý các độ phân giải cao; 2. Tiêu thụ ít tài nguyên khi xử lý độ phân giải cao; 3. Sử dụng ít thông tin đại diện cho hình ảnh; 4. Hỗ trợ các đầu vào có độ phân giải khác nhau; 5. Có số lượng tham số vừa phải. Tuy nhiên, như đã mô tả ở Phần 2.1, các bộ mã hóa mã nguồn mở hiện có không thể đáp ứng đầy đủ tất cả các yêu cầu trên. Do đó, chúng tôi đã tự thiết kế một bộ mã hóa hình ảnh mới, có tên là DeepEncoder.

---

**English:** <|ref|>title<|/ref|><|det|>[[117, 688, 400, 704]]<|/det|>
#### 3.2.1. Architecture of DeepEncoder  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[117, 688, 400, 704]]<|/det|>
#### 3.2.1. Cấu trúc của DeepEncoder

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 714, 882, 891]]<|/det|>
DeepEncoder mainly consists of two components: a visual perception feature extraction component dominated by window attention, and a visual knowledge feature extraction component with dense global attention. To benefit from the pretraining gains of previous works, we use SAM- base (patch- size 16) and CLIP- large as the main architectures for the two components respectively. For CLIP, we remove the first patch embedding layer since its input is no longer images but output tokens from the previous pipeline. Between the two components, we borrow from Vary [36] and use a 2- layer convolutional module to perform \(16\times\) downsampling of vision tokens. Each convolutional layer has a kernel size of 3, stride of 2, padding of 1, and channels increase from 256 to 1024. Assuming we input a \(1024\times 1024\) image, the DeepEncoder will segment it into \(1024 / 16\times 1024 / 16 = 4096\) patch tokens. Since the first half of encoder is dominated by window attention and only 80M, the activation is acceptable. Before entering global attention,

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 714, 882, 891]]<|/det|>  
DeepEncoder chủ yếu bao gồm hai thành phần: một thành phần trích xuất các đặc điểm liên quan đến khả năng nhận diện hình ảnh, được điều khiển bởi thuật toán chú ý theo cửa sổ; và một thành phần trích xuất các đặc điểm kiến thức hình ảnh, sử dụng thuật toán chú ý toàn cục. Để tận dụng những lợi ích từ các nghiên cứu trước đây về việc huấn luyện sơ bộ, chúng tôi lựa chọn SAM-base (kích thước khối dữ liệu 16) và CLIP-large làm cấu trúc chính cho hai thành phần này. Đối với CLIP, chúng tôi loại bỏ lớp đưa dữ liệu vào dạng khối đầu tiên, vì đầu vào của nó không còn là hình ảnh nữa mà là các mã hóa từ các quá trình xử lý trước đó. Giữa hai thành phần này, chúng tôi áp dụng mô-đun hội tụ 2 lớp theo phương pháp Vary [36] để thực hiện việc giảm kích thước các mã hóa hình ảnh xuống còn \(16\times\). Mỗi lớp hội tụ có kích thước kernel là 3, bước chuyển động là 2, độ đầy là 1, và số kênh tín hiệu tăng từ 256 lên 1024. Nếu chúng ta đưa vào một hình ảnh có kích thước \(1024 \times 1024\), DeepEncoder sẽ chia nó thành \(1024 / 16 \times 1024 / 16 = 4096\) mã hóa hình ảnh. Vì nửa đầu của hệ thống này chủ yếu sử dụng thuật toán chú ý theo cửa sổ và chỉ tốn bộ nhớ 80MB, nên mức độ kích hoạt của các thành phần này vẫn được coi là chấp nhận được. Trước khi các mã hóa này được đưa vào quá trình xử lý bằng thuật toán chú ý toàn cục…

---

**English:** 
============================================================
--- Page 6 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 6 ---
============================================================

---

**English:** ![Image 0_0](images/page_6_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 269, 881, 318]]<|/det|>
<center>Figure 4 | To test model performance under different compression ratios (requiring different numbers of vision tokens) and enhance the practicality of DeepSeek-OCR, we configure it with multiple resolution modes. </center>  

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_6_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 269, 881, 318]]<|/thông tin chi tiết|>
<center>Hình 4: Để kiểm tra hiệu suất của mô hình ở các tỷ lệ nén khác nhau (đòi hỏi số lượng “token hình ảnh” khác nhau) và nâng cao tính ứng dụng thực tế của DeepSeek-OCR, chúng tôi đã cấu hình nó với nhiều chế độ độ phân giải khác nhau.</center>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 342, 881, 376]]<|/det|>
the 4096 tokens go through the compression module and the token count becomes \(4096 / 16 = 256\) , thus making the overall activation memory controllable.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 342, 881, 376]]<|/det|>
the 4096 tokens go through the compression module and the token count becomes \(4096 / 16 = 256\), thus making the overall activation memory controllable.<|ref|>text<|/ref|><|det|>[[115, 342, 881, 376]]<|/det|>  
4096 ký hiệu này được đưa qua mô-đun nén; sau đó, số lượng các ký hiệu này giảm xuống còn \(4096 \div 16 = 256\). Nhờ vậy, tổng dung lượng bộ nhớ cần thiết để xử lý dữ liệu trở nên có thể kiểm soát được.

---

**English:** <|ref|>table<|/ref|><|det|>[[166, 431, 829, 535]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[115, 386, 881, 420]]<|/det|>
Table 1 | Multi resolution support of DeepEncoder. For both research and application purposes, we design DeepEncoder with diverse native resolution and dynamic resolution modes.   

**Tiếng Việt:** <|ref|>biểu bảng<|/ref|><|thông tin|>[[166, 431, 829, 535]]<|/thông tin|>
<|ref|>chú thích biểu bảng<|/ref|><|thông tin|>[[115, 386, 881, 420]]<|/thông tin|>
Bảng 1 | Khả năng hỗ trợ nhiều độ phân giải của DeepEncoder. Vì mục đích nghiên cứu lẫn ứng dụng, chúng tôi đã thiết kế DeepEncoder với nhiều độ phân giải khác nhau và các chế độ điều chỉnh độ phân giải một cách linh hoạt.

---

**English:** <table><tr><td rowspan="2">Mode</td><td colspan="4">Native Resolution</td><td colspan="2">Dynamic Resolution</td></tr><tr><td>Tiny</td><td>Small</td><td>Base</td><td>Large</td><td>Gundam</td><td>Gundam-M</td></tr><tr><td>Resolution</td><td>512</td><td>640</td><td>1024</td><td>1280</td><td>640+1024</td><td>1024+1280</td></tr><tr><td>Tokens</td><td>64</td><td>100</td><td>256</td><td>400</td><td>n×100+256</td><td>n×256+400</td></tr><tr><td>Process</td><td colspan="3">resize resize padding padding</td><td colspan="3">resize + padding resize + padding</td></tr></table>  

**Tiếng Việt:** <table><tr><td rowspan="2">Chế độ</td><td colspan="4">Độ phân giải gốc</td><td colspan="2">Độ phân giải động</td></tr><tr><td>Tiny</td><td>Small</td><td>Base</td><td>Large</td><td>Gundam</td><td>Gundam-M</td></tr><tr><td>Độ phân giải</td><td>512</td><td>640</td><td>1024</td><td>1280</td><td>640+1024</td><td>1024+1280</td></tr><tr><td>Số khối điểm ảnh</td><td>64</td><td>100</td><td>256</td><td>400</td><td>n×100+256</td><td>n×256+400</td></tr><tr><td>Quy trình xử lý hình ảnh</td><td colspan="3">Thay đổi kích thước hình ảnh + tăng/không gian viền</td><td colspan="3">Thay đổi kích thước hình ảnh + tăng/không gian viền</td></tr></table>

---

**English:** <|ref|>title<|/ref|><|det|>[[117, 560, 396, 576]]<|/det|>
#### 3.2.2. Multiple resolution support  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[117, 560, 396, 576]]<|/det|>
#### 3.2.2. Hỗ trợ nhiều độ phân giải khác nhau

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 586, 881, 636]]<|/det|>
Suppose we have an image with 1000 optical characters and we want to test how many vision tokens are needed for decoding. This requires the model to support a variable number of vision tokens. That is to say the DeepEncoder needs to support multiple resolutions.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 586, 881, 636]]<|/det|>  
Giả sử chúng ta có một hình ảnh chứa 1000 ký tự quang học và muốn kiểm tra xem cần bao nhiêu “token thị giác” để giải mã hình ảnh đó. Điều này đòi hỏi mô hình phải hỗ trợ việc sử dụng một số lượng khác nhau các “token thị giác”; nói cách khác, bộ mã hóa sâu (DeepEncoder) cần phải hỗ trợ nhiều độ phân giải khác nhau.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 642, 881, 725]]<|/det|>
We meet the requirement aforementioned through dynamic interpolation of positional encodings, and design several resolution modes for simultaneous model training to achieve the capability of a single DeepSeek- OCR model supporting multiple resolutions. As shown in Figure 4, DeepEncoder mainly supports two major input modes: native resolution and dynamic resolution. Each of them contains multiple sub- modes.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 642, 881, 725]]<|/det|>  
Chúng tôi đã đáp ứng được yêu cầu nêu trên thông qua phương pháp giải quyết động dựa trên các mã hóa vị trí, đồng thời thiết kế nhiều chế độ độ phân giải khác nhau để thực hiện việc huấn luyện mô hình đồng thời, nhằm đảm bảo rằng một mô hình DeepSeek-OCR duy nhất có thể hỗ trợ nhiều độ phân giải khác nhau. Như được minh họa trong Hình 4, DeepEncoder chủ yếu hỗ trợ hai chế độ đầu vào chính: độ phân giải gốc và độ phân giải động. Mỗi chế độ đều bao gồm nhiều tiểu chế độ con khác nhau.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 731, 881, 844]]<|/det|>
Native resolution supports four sub- modes: Tiny, Small, Base, and Large, with corresponding resolutions and token counts of \(512 \times 512\) (64), \(640 \times 640\) (100), \(1024 \times 1024\) (256), and \(1280 \times 1280\) (400) respectively. Since Tiny and Small models have relatively small resolutions, to avoid wasting vision tokens, images are processed by directly resizing the original shape. For Base and Large modes, in order to preserve the original image aspect ratio, images are padded to the corresponding size. After padding, the number of valid vision tokens is less than the actual number of vision tokens, with the calculation formula being:  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 731, 881, 844]]<|/det|>  
Độ phân giải gốc hỗ trợ bốn chế độ con: Tiny, Small, Base và Large, với các độ phân giải và số lượng “token” tương ứng là \(512 \times 512\) (64), \(640 \times 640\) (100), \(1024 \times 1024\) (256) và \(1280 \times 1280\) (400). Vì các mô hình Tiny và Small có độ phân giải tương đối thấp, để tránh lãng phí các “token” xử lý hình ảnh, các hình ảnh này được điều chỉnh kích thước trực tiếp mà không thay đổi tỷ lệ khung hình ban đầu. Đối với các chế độ Base và Large, để bảo toàn tỷ lệ khung hình gốc, các hình ảnh sẽ được điền thêm ký tự để đạt đến kích thước mong muốn. Sau khi điền thêm ký tự, số lượng “token” hợp lệ sẽ ít hơn số lượng “token” thực tế; công thức tính toán số lượng “token” hợp lệ như sau:

---

**English:** <|ref|>equation<|/ref|><|det|>[[250, 855, 880, 874]]<|/det|>
\[N_{valid} = \lceil N_{actual}\times [1 - ((max(w,h) - min(w,h)) / (max(w,h)))]\rceil \quad (1)\]  

**Tiếng Việt:** <|ref|>phương trình<|/ref|><|det|>[[250, 855, 880, 874]]<|/det|>
\[N_{hợp lệ} = \lceil N_{thực tế} \times \left[1 - \left(\frac{max(w,h) - min(w,h)}{max(w,h)}\right)\right]\rceil \quad (1)\]

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 885, 716, 902]]<|/det|>
where \(w\) and \(h\) represent the width and height of the original input image.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 885, 716, 902]]<|/det|>  
Trong đó, \(w\) và \(h\) lần lượt là độ rộng và độ cao của hình ảnh đầu vào ban đầu.

---

**English:** 
============================================================
--- Page 7 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 7 ---
============================================================

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 100, 883, 262]]<|/det|>
Dynamic resolution can be composed of two native resolutions. For example, Gundam mode consists of \(n \times 640 \times 640\) tiles (local views) and a \(1024 \times 1024\) global view. The tiling method following InternVL2.0 [8]. Supporting dynamic resolution is mainly for application considerations, especially for ultra- high- resolution inputs (such as newspaper images). Tiling is a form of secondary window attention that can effectively reduce activation memory further. It's worth noting that due to our relatively large native resolutions, images won't be fragmented too much under dynamic resolution (the number of tiles is controlled within the range of 2 to 9). The vision token number output by the DeepEncoder under Gundam mode is: \(n \times 100 + 256\) , where \(n\) is the number of tiles. For images with both width and height smaller than 640, \(n\) is set to 0, i.e., Gundam mode will degrade to Base mode.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 100, 883, 262]]<|/det|>
Dynamic resolution can be composed of two native resolutions. For example, Gundam mode consists of \(n \times 640 \times 640\) tiles (local views) and a \(1024 \times 1024\) global view. The tiling method following InternVL2.0 [8]. Supporting dynamic resolution is mainly for application considerations, especially for ultra- high- resolution inputs (such as newspaper images). Tiling is a form of secondary window attention that can effectively reduce activation memory further. It's worth noting that due to our relatively large native resolutions, images won't be fragmented too much under dynamic resolution (the number of tiles is controlled within the range of 2 to 9). The vision token number output by the DeepEncoder under Gundam mode is: \(n \times 100 + 256\), where \(n\) is the number of tiles. For images with both width and height smaller than 640, \(n\) is set to 0, i.e., Gundam mode will degrade to Base mode.<|ref|>text<|/ref|><|det|>[[115, 100, 883, 262]]<|/det|>  
Độ phân giải động có thể được tạo thành từ hai độ phân giải gốc khác nhau. Ví dụ, chế độ Gundam bao gồm các ô hình ảnh có kích thước \(n \times 640 \times 640\) và một hình ảnh tổng thể có kích thước \(1024 \times 1024\). Phương pháp sắp xếp các ô này tuân theo tiêu chuẩn InternVL2.0 [8]. Việc hỗ trợ độ phân giải động chủ yếu nhằm phục vụ các ứng dụng cụ thể, đặc biệt là đối với các nguồn dữ liệu có độ phân giải siêu cao (chẳng hạn như hình ảnh trên báo chí). Phương pháp này giúp giảm đáng kể lượng bộ nhớ cần thiết để xử lý dữ liệu hình ảnh. Đáng chú ý là do độ phân giải gốc của chúng ta khá lớn, nên khi sử dụng độ phân giải động, hình ảnh không bị phân mảnh quá nhiều (số lượng các ô hình ảnh được kiểm soát trong khoảng từ 2 đến 9). Số lượng các “token hình ảnh” được tạo ra bởi thuật toán DeepEncoder trong chế độ Gundam là \(n \times 100 + 256\), trong đó \(n\) là số lượng các ô hình ảnh. Đối với những hình ảnh có chiều rộng và chiều cao nhỏ hơn 640, giá trị của \(n\) sẽ được đặt thành 0; trong trường hợp này, chế độ Gundam sẽ tự động chuyển sang chế độ Base.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 270, 883, 350]]<|/det|>
Gundam mode is trained together with the four native resolution modes to achieve the goal of one model supporting multiple resolutions. Note that Gundam- master mode ( \(1024 \times 1024\) local views \(+ 1280 \times 1280\) global view) is obtained through continued training on a trained DeepSeek- OCR model. This is mainly for load balancing, as Gundam- master's resolution is too large and training it together would slow down the overall training speed.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 270, 883, 350]]<|/det|>  
Chế độ Gundam được huấn luyện cùng với bốn chế độ độ phân giải khác nhau nhằm mục đích tạo ra một mô hình có thể hỗ trợ nhiều độ phân giải khác nhau. Lưu ý rằng chế độ Gundam-Master (gồm 115×1024 điểm ảnh cục bộ + 1280×1280 điểm ảnh toàn cảnh) được xây dựng thông qua việc tiếp tục huấn luyện trên mô hình DeepSeek-OCR đã được đào tạo trước đó. Việc này chủ yếu nhằm đảm bảo sự cân bằng trong quá trình huấn luyện; bởi vì độ phân giải của chế độ Gundam-Master quá lớn, và việc huấn luyện nó cùng với các chế độ khác sẽ làm chậm tốc độ tổng thể của quá trình đào tạo.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 372, 306, 388]]<|/det|>
### 3.3. The MoE Decoder  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 372, 306, 388]]<|/det|>
### 3.3. Bộ giải mã MoE

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 398, 883, 480]]<|/det|>
Our decoder uses the DeepSeekMoE [19, 20], specifically DeepSeek- 3B- MoE. During inference, the model activates 6 out of 64 routed experts and 2 shared experts, with about 570M activated parameters. The 3B DeepSeekMoE is very suitable for domain- centric (OCR for us) VLM research, as it obtains the expressive capability of a 3B model while enjoying the inference efficiency of a 500M small model.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 398, 883, 480]]<|/det|>  
Bộ giải mã của chúng tôi sử dụng công nghệ DeepSeekMoE [19, 20], cụ thể là mô hình DeepSeek-3B-MoE. Trong quá trình thực hiện các phép tính dự đoán, mô hình này kích hoạt 6 trong tổng số 64 mô-đun chuyên biệt và 2 mô-đun chung, với khoảng 570 triệu tham số được sử dụng trong quá trình tính toán. Mô hình DeepSeekMoE 3B rất phù hợp cho các nghiên cứu về các hệ thống trí tuệ nhân tạo tập trung vào từng lĩnh vực cụ thể (chẳng hạn như công nghệ nhận diện chữ viết tay), bởi vì nó vừa giữ được khả năng xử lý thông tin mạnh mẽ của các mô hình có dung lượng lớn, vừa sở hữu hiệu suất tính toán cao như các mô hình nhỏ hơn.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 488, 880, 520]]<|/det|>
The decoder reconstructs the original text representation from the compressed latent vision tokens of DeepEncoder as:  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 488, 880, 520]]<|/det|>  
Bộ giải mã sẽ tái tạo lại dạng biểu diễn văn bản gốc từ các mã hóa ẩn chứa được tạo ra bởi DeepEncoder như sau:

---

**English:** <|ref|>equation<|/ref|><|det|>[[278, 530, 880, 550]]<|/det|>
\[f_{\mathrm{dec}}:\mathbb{R}^{n\times d_{\mathrm{latent}}}\to \mathbb{R}^{N\times d_{\mathrm{text}}}; \quad \hat{\mathbf{X}} = f_{\mathrm{dec}}(\mathbf{Z})\quad \mathrm{where} n\leq N \quad (2)\]  

**Tiếng Việt:** <|ref|>phương trình<|/ref|><|det|>[[278, 530, 880, 550]]<|/det|>
\[f_{\mathrm{dec}}:\mathbb{R}^{n\times d_{\mathrm{latent}}}\to \mathbb{R}^{N\times d_{\mathrm{text}}}; \quad \hat{\mathbf{X}} = f_{\mathrm{dec}}(\mathbf{Z})\quad \text{trong đó} n\leq N \quad (2)\]

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 560, 881, 643]]<|/det|>
where \(\mathbf{Z} \in \mathbb{R}^{n \times d_{\mathrm{latent}}}\) are the compressed latent(vision) tokens from DeepEncoder and \(\hat{\mathbf{X}} \in \mathbb{R}^{N \times d_{\mathrm{text}}}\) is the reconstructed text representation. The function \(f_{\mathrm{dec}}\) represents a non- linear mapping that can be effectively learned by compact language models through OCR- style training. It is reasonable to conjecture that LLMs, through specialized pretraining optimization, would demonstrate more natural integration of such capabilities.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 560, 881, 643]]<|/det|>  
Trong đó, \(\mathbf{Z} \in \mathbb{R}^{n \times d_{\mathrm{latent}}}\) là các token ẩn được nén ra từ mô hình DeepEncoder, còn \(\hat{\mathbf{X}} \in \mathbb{R}^{N \times d_{\mathrm{text}}}\) là biểu diễn văn bản được tái tạo lại. Hàm \(f_{\mathrm{dec}}\) đại diện cho một phép ánh xạ phi tuyến tính; phép ánh xạ này có thể được học một cách hiệu quả thông qua các mô hình ngôn ngữ được huấn luyện theo phương pháp OCR. Có thể suy đoán rằng các mô hình LLM, nhờ vào các quá trình tối ưu hóa huấn luyện chuyên biệt, sẽ thể hiện khả năng tích hợp những công nghệ này một cách tự nhiên hơn.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 667, 258, 682]]<|/det|>
### 3.4. Data Engine  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 667, 258, 682]]<|/det|>
### 3.4. Máy chạy dữ liệu

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 692, 883, 790]]<|/det|>
We construct complex and diverse training data for DeepSeek- OCR, including OCR 1.0 data, which mainly consists of traditional OCR tasks such as scene image OCR and document OCR; OCR 2.0 data, which mainly includes parsing tasks for complex artificial images, such as common charts, chemical formulas, and plane geometry parsing data; General vision data, which is mainly used to inject certain general image understanding capabilities into DeepSeek- OCR and preserve the general vision interface.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 692, 883, 790]]<|/det|>  
Chúng tôi đã xây dựng những bộ dữ liệu huấn luyện phức tạp và đa dạng cho hệ thống DeepSeek-OCR, bao gồm:  
– Dữ liệu OCR 1.0, chủ yếu bao gồm các nhiệm vụ OCR truyền thống như nhận diện văn bản trong hình ảnh hay tài liệu;  
– Dữ liệu OCR 2.0, tập trung vào việc phân tích các hình ảnh nhân tạo phức tạp, chẳng hạn như biểu đồ thông dụng, công thức hóa học hay cấu trúc hình học;  
– Dữ liệu thị giác tổng quát, nhằm trang bị cho DeepSeek-OCR khả năng hiểu biết về hình ảnh một cách tổng quát hơn, đồng thời giữ nguyên giao diện thị giác cơ bản của hệ thống.

---

**English:** <|ref|>title<|/ref|><|det|>[[115, 810, 279, 825]]<|/det|>
#### 3.4.1. OCR 1.0 data  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[115, 810, 279, 825]]<|/det|>
#### Dữ liệu OCR 1.0

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 835, 881, 900]]<|/det|>
Document data is the top priority for DeepSeek- OCR. We collect 30M pages of diverse PDF data covering about 100 languages from the Internet, with Chinese and English accounting for approximately 25M and other languages accounting for 5M. For this data, we create two types of ground truth: coarse annotations and fine annotations. Coarse annotations are extracted

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 835, 881, 900]]<|/det|>  
Dữ liệu tài liệu là ưu tiên hàng đầu đối với công cụ DeepSeek-OCR. Chúng tôi đã thu thập được 30 triệu trang tài liệu dạng PDF đa dạng ngôn ngữ từ Internet; trong đó, các tài liệu bằng tiếng Trung và tiếng Anh chiếm khoảng 25 triệu trang, còn các ngôn ngữ khác chiếm 5 triệu trang. Đối với những dữ liệu này, chúng tôi đã tạo ra hai loại ghi chú chuẩn xác: ghi chú sơ lược và ghi chú chi tiết. Các ghi chú sơ lược được rút ra từ dữ liệu thu thập được…

---

**English:** 
============================================================
--- Page 8 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 8 ---
============================================================

---

**English:** ![Image 0_0](images/page_8_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 454, 881, 503]]<|/det|>
<center>Figure 5 | OCR 1.0 fine annotations display. We format the ground truth into an interleaved layout and text format, where each paragraph of text is preceded by the coordinates and label of it in the original image. All coordinates are normalized into 1000 bins. </center>  

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_8_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin|>[[115, 454, 881, 503]]<|/thông tin|>
<center>Hình 5 | Các ghi chú chi tiết từ công cụ OCR 1.0 được hiển thị ở đây. Chúng tôi đã định dạng dữ liệu tham chiếu theo dạng xen kẽ giữa các đoạn văn bản và thông tin địa lý; trước mỗi đoạn văn bản đều được ghi rõ tọa độ và nhãn của nó trong hình ảnh gốc. Tất cả các tọa độ đều được quy đổi sang khoảng từ 0 đến 1000.</center>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 526, 882, 737]]<|/det|>
directly from the full dataset using fitz, aimed at teaching the model to recognize optical text, especially in minority languages. Fine annotations include 2M pages each for Chinese and English, labeled using advanced layout models (such as PP- DocLayout [33]) and OCR models (such as MinuerU [34] and GOT- OCR2.0 [38]) to construct detection and recognition interleaved data. For minority languages, in the detection part, we find that the layout model enjoys certain generalization capabilities. In the recognition part, we use fitz to create small patch data to train a GOT- OCR2.0, then use the trained model to label small patches after layout processing, employing a model flywheel to create 600K data samples. During the training of DeepSeek- OCR, coarse labels and fine labels are distinguished using different prompts. The ground truth for fine annotation image- text pairs can be seen in Figure 5. We also collect 3M Word data, constructing high- quality image- text pairs without layout by directly extracting content. This data mainly brings benefits to formulas and HTML- formatted tables. Additionally, we select some open- source data [28, 37] as supplements.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 526, 882, 737]]<|/det|>  
Dữ liệu này được thu thập trực tiếp từ tập dữ liệu đầy đủ bằng công cụ fitz, với mục đích huấn luyện mô hình nhằm giúp nó nhận diện văn bản được hiển thị trên màn hình, đặc biệt là các văn bản được viết bằng các ngôn ngữ thiểu số. Các bộ ghi chú chi tiết bao gồm 2 triệu trang văn bản tiếng Trung và tiếng Anh; chúng được đánh dấu bằng các mô hình bố cục tiên tiến (như PP-DocLayout [33]) và các công cụ OCR (như MinuerU [34] và GOT-OCR2.0 [38]) để tạo ra dữ liệu phục vụ cho quá trình nhận diện. Đối với các ngôn ngữ thiểu số, trong phần xác định cấu trúc văn bản, chúng tôi nhận thấy rằng các mô hình bố cục này có khả năng tổng quát hóa tốt. Trong phần nhận diện văn bản, chúng tôi sử dụng công cụ fitz để tạo ra các đoạn văn bản nhỏ để huấn luyện mô hình GOT-OCR2.0; sau đó, dùng mô hình đã được huấn luyện này để đánh dấu các đoạn văn bản sau khi chúng được xử lý về mặt bố cục, từ đó tạo ra 600.000 mẫu dữ liệu. Trong quá trình huấn luyện mô hình DeepSeek-OCR, các nhãn đánh dấu cơ bản và chi tiết được sử dụng các thông tin khác nhau để phân biệt. Các cặp hình ảnh kèm văn bản được sử dụng để đánh giá chất lượng của các bộ ghi chú chi tiết có thể được xem ở Hình 5. Chúng tôi cũng thu thập thêm 3 triệu bộ dữ liệu văn bản, từ đó tạo ra các cặp hình ảnh-không-gian văn bản chất lượng cao mà không cần thông tin về bố cục văn bản; những dữ liệu này đặc biệt hữu ích đối với các công thức toán học và các bảng biểu định dạng HTML. Ngoài ra, chúng tôi cũng sử dụng một số tài nguyên mã nguồn mở [28, 37] như tài liệu bổ sung cho quá trình nghiên cứu này.

---

**English:** <|ref|>text<|/ref|><|det|>[[116, 743, 881, 810]]<|/det|>
For natural scene OCR, our model mainly supports Chinese and English. The image data sources come from LAION [31] and Wukong [13], labeled using PaddleOCR [9], with 10M data samples each for Chinese and English. Like document OCR, natural scene OCR can also control whether to output detection boxes through prompts.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[116, 743, 881, 810]]<|/det|>  
Đối với công nghệ nhận dạng ký tự trong hình ảnh các cảnh vật tự nhiên, mô hình của chúng tôi hỗ trợ chủ yếu tiếng Trung và tiếng Anh. Các nguồn dữ liệu hình ảnh được lấy từ LAION [31] và Wukong [13], và đã được đánh dấu bằng công cụ PaddleOCR [9]; mỗi nguồn chứa 10 triệu mẫu dữ liệu dành cho tiếng Trung và tiếng Anh. Tương tự như công nghệ nhận dạng ký tự trong tài liệu, công nghệ này cũng cho phép người dùng điều khiển việc có hiển thị các khung xác định vị trí ký tự hay không thông qua các lệnh chỉ đạo cụ thể.

---

**English:** <|ref|>title<|/ref|><|det|>[[116, 828, 280, 844]]<|/det|>
#### 3.4.2. OCR 2.0 data  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[116, 828, 280, 844]]<|/det|>
#### Dữ liệu OCR 2.0

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 854, 881, 887]]<|/det|>
Following GOT- OCR2.0 [38], we refer to chart, chemical formula, and plane geometry parsing data as OCR 2.0 data. For chart data, following OneChart [7], we use pyecharts and matplotlib

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 854, 881, 887]]<|/det|>  
Theo tiêu chuẩn GOT-OCR2.0 [38], chúng tôi coi dữ liệu biểu đồ, công thức hóa học và thông tin liên quan đến hình học phẳng là dữ liệu OCR 2.0. Đối với dữ liệu biểu đồ, theo hướng dẫn của OneChart [7], chúng tôi sử dụng các thư viện pyecharts và matplotlib để xử lý dữ liệu này.

---

**English:** 
============================================================
--- Page 9 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 9 ---
============================================================

---

**English:** ![Image 0_0](images/page_9_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 240, 881, 321]]<|/det|>
<center>Figure 6 | For charts, we do not use OneChart's [7] dictionary format, but instead use HTML table format as labels, which can save a certain amount of tokens. For plane geometry, we convert the ground truth to dictionary format, where the dictionary contains keys such as line segments, endpoint coordinates, line segment types, etc., for better readability. Each line segment is encoded using the Slow Perception [39] manner. </center>  

**Tiếng Việt:** ![Hình 0_0](images/page_9_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 240, 881, 321]]<|/thông tin chi tiết|>
<center>Hình 6: Đối với các biểu đồ, chúng tôi không sử dụng định dạng từ điển [7] của công cụ OneChart, mà thay vào đó sử dụng định dạng bảng HTML cho các tiêu đề biểu đồ; cách này giúp tiết kiệm được một lượng lớn dung lượng lưu trữ. Đối với các đối tượng hình học phẳng, chúng tôi chuyển đổi dữ liệu thực tế thành định dạng từ điển, trong đó các khóa bao gồm tên các đoạn thẳng, tọa độ hai đầu mút của đoạn thẳng, loại đoạn thẳng, v.v., nhằm tăng tính dễ đọc. Mỗi đoạn thẳng đều được mã hóa theo phương pháp Slow Perception [39].</center>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 345, 882, 508]]<|/det|>
to render 10M images, mainly including commonly used line, bar, pie, and composite charts. We define chart parsing as image- to- HTML- table conversion task, as shown in Figure 6(a). For chemical formulas, we utilize SMILES format from PubChem as the data source and render them into images using RDKit, constructing 5M image- text pairs. For plane geometry images, we follow Slow Perception [39] for generation. Specifically, we use perception- ruler size as 4 to model each line segment. To increase the diversity of rendered data, we introduce geometric translation- invariant data augmentation, where the same geometric image is translated in the original image, corresponding to the same ground truth drawn at the centered position in the coordinate system. Based on this, we construct a total of 1M plane geometry parsing data, as illustrated in Figure 6(b).  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 345, 882, 508]]<|/det|>  
Để hiển thị 10 triệu hình ảnh, chủ yếu bao gồm các loại biểu đồ dạng đường thẳng, thanh, phần trăm và biểu đồ tổng hợp thường được sử dụng, chúng tôi coi việc xử lý dữ liệu biểu đồ là quá trình chuyển đổi các hình ảnh đó thành các bảng dữ liệu dạng HTML, như được minh họa trong Hình 6(a). Đối với các công thức hóa học, chúng tôi sử dụng định dạng SMILES từ PubChem làm nguồn dữ liệu và sử dụng công cụ RDKit để chuyển đổi chúng thành hình ảnh, tạo ra tổng cộng 5 triệu cặp dữ liệu hình ảnh-không gian văn bản. Đối với các hình ảnh hình học phẳng, chúng tôi áp dụng phương pháp Slow Perception [39] để tạo ra chúng; cụ thể, chúng tôi sử dụng kích thước “thước đo” là 4 để mô hình hóa từng đoạn thẳng trong hình ảnh. Nhằm tăng đa dạng của dữ liệu được hiển thị, chúng tôi cũng áp dụng phương pháp tăng cường dữ liệu dựa trên nguyên lý bất biến hình học; cụ thể, cùng một hình ảnh hình học sẽ được dịch chuyển theo các hướng khác nhau so với vị trí ban đầu, sao cho điểm đầu và điểm cuối của đoạn thẳng vẫn nằm tại cùng một vị trí trong hệ tọa độ. Dựa trên các phương pháp này, chúng tôi đã tạo ra tổng cộng 1 triệu bộ dữ liệu hình học phẳng, như được minh họa trong Hình 6(b).

---

**English:** <|ref|>title<|/ref|><|det|>[[117, 527, 330, 543]]<|/det|>
#### 3.4.3. General vision data  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[117, 527, 330, 543]]<|/det|>
#### 3.4.3. Dữ liệu hình ảnh tổng quát

---

**English:** <|ref|>text<|/ref|><|det|>[[116, 553, 881, 666]]<|/det|>
DeepEncoder can benefit from CLIP's pretraining gains and has sufficient parameters to incorporate general visual knowledge. Therefore, we also prepare some corresponding data for DeepSeek- OCR. Following DeepSeek- VL2 [40], we generate relevant data for tasks such as caption, detection, and grounding. Note that DeepSeek- OCR is not a general VLM model, and this portion of data accounts for only \(20\%\) of the total data. We introduce such type of data mainly to preserve the general vision interface, so that researchers interested in our model and general vision task can conveniently advance their work in the future.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[116, 553, 881, 666]]<|/det|>  
DeepEncoder có thể hưởng lợi từ những kết quả đạt được trong quá trình huấn luyện sơ bộ của CLIP, đồng thời cũng sở hữu đủ số lượng tham số để tiếp nhận các kiến thức thị giác tổng quát. Do đó, chúng tôi cũng đã chuẩn bị một số dữ liệu phù hợp cho DeepSeek-OCR. Theo hướng dẫn của DeepSeek-VL2 [40], chúng tôi đã tạo ra các dữ liệu liên quan đến các nhiệm vụ như việc gán chú thích cho hình ảnh, phát hiện đối tượng và xác định mối quan hệ giữa các đối tượng trong hình ảnh. Lưu ý rằng DeepSeek-OCR không phải là một mô hình VLM tổng quát; phần dữ liệu này chỉ chiếm khoảng \(20\%\) tổng lượng dữ liệu tổng thể. Chúng tôi cung cấp loại dữ liệu này chủ yếu nhằm bảo đảm tính tổng quát của công cụ thị giác này, giúp các nhà nghiên cứu quan tâm đến mô hình của chúng tôi và các nhiệm vụ thị giác nói chung có thể tiếp tục phát triển công trình nghiên cứu của mình một cách thuận lợi trong tương lai.

---

**English:** <|ref|>title<|/ref|><|det|>[[117, 686, 288, 702]]<|/det|>
#### 3.4.4. Text-only data  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[117, 686, 288, 702]]<|/det|>
#### 3.4.4. Dữ liệu chỉ chứa văn bản

---

**English:** <|ref|>text<|/ref|><|det|>[[117, 712, 881, 777]]<|/det|>
To ensure the model's language capabilities, we introduced \(10\%\) of in- house text- only pretrain data, with all data processed to a length of 8192 tokens, which is also the sequence length for DeepSeek- OCR. In summary, when training DeepSeek- OCR, OCR data accounts for \(70\%\) , general vision data accounts for \(20\%\) , and text- only data accounts for \(10\%\) .  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[117, 712, 881, 777]]<|/det|>
To ensure the model's language capabilities, we introduced \(10\%\) of in- house text- only pretrain data, with all data processed to a length of 8192 tokens, which is also the sequence length for DeepSeek- OCR. In summary, when training DeepSeek- OCR, OCR data accounts for \(70\%\), general vision data accounts for \(20\%\), and text- only data accounts for \(10\%\).<|ref|>text<|/ref|><|det|>[[117, 712, 881, 777]]<|/det|>  
Để đảm bảo khả năng xử lý ngôn ngữ của mô hình, chúng tôi đã sử dụng 10% dữ liệu được huấn luyện trước chỉ chứa văn bản, trong đó tất cả các dữ liệu đều được xử lý sao cho có độ dài bằng 8192 ký tự – đây cũng chính là độ dài chuỗi dữ liệu được sử dụng trong DeepSeek-OCR. Nói chung, khi huấn luyện DeepSeek-OCR, dữ liệu OCR chiếm 70%, dữ liệu thị giác thông thường chiếm 20%, và dữ liệu chỉ chứa văn bản chiếm 10%.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 800, 309, 817]]<|/det|>
### 3.5. Training Pipelines  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 800, 309, 817]]<|/det|>
### 3.5. Quy trình đào tạo mô hình</td>

---

**English:** <|ref|>text<|/ref|><|det|>[[117, 827, 881, 891]]<|/det|>
Our training pipeline is very simple and consists mainly of two stages: a). Training DeepEncoder independently; b). Training the DeepSeek- OCR. Note that the Gundam- master mode is obtained by continuing training on a pre- trained DeepSeek- OCR model with 6M sampled data. Since the training protocol is identical to other modes, we omit the detailed description hereafter.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[117, 827, 881, 891]]<|/det|>  
Quy trình đào tạo của chúng tôi rất đơn giản và bao gồm hai giai đoạn chính: a) Đào tạo riêng bộ công cụ DeepEncoder; b) Đào tạo hệ thống DeepSeek-OCR. Lưu ý rằng chế độ “Gundam-master” được tạo ra bằng cách tiếp tục đào tạo mô hình DeepSeek-OCR đã được huấn luyện sẵn, sử dụng 6 triệu dữ liệu mẫu. Vì quy trình đào tạo này giống hệt với các chế độ khác, chúng tôi sẽ không trình bày chi tiết thêm ở đây.

---

**English:** 
============================================================
--- Page 10 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 10 ---
============================================================

---

**English:** <|ref|>title<|/ref|><|det|>[[115, 101, 348, 116]]<|/det|>
#### 3.5.1. Training DeepEncoder  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[115, 101, 348, 116]]<|/det|>
#### 3.5.1. Đào tạo mô hình DeepEncoder

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 127, 881, 207]]<|/det|>
3.5.1. Training DeepEncoderFollowing Vary [36], we utilize a compact language model [15] and use the next token prediction framework to train DeepEncoder. In this stage, we use all OCR 1.0 and 2.0 data aforementioned, as well as 100M general data sampled from the LAION [31] dataset. All data is trained for 2 epochs with a batch size of 1280, using the AdamW [23] optimizer with cosine annealing scheduler [22] and a learning rate of 5e- 5. The training sequence length is 4096.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 127, 881, 207]]<|/det|>  
3.5.1. Đào tạo DeepEncoder  
Theo phương pháp được đề xuất trong [36], chúng tôi sử dụng một mô hình ngôn ngữ gọn nhẹ [15] và áp dụng cấu trúc dự đoán các ký tự tiếp theo để đào tạo DeepEncoder. Trong giai đoạn này, chúng tôi sử dụng toàn bộ dữ liệu từ các bộ dữ liệu OCR 1.0 và 2.0 đã nêu trên, cùng với 100 triệu dữ liệu thông thường được lấy mẫu từ bộ dữ liệu LAION [31]. Tất cả các dữ liệu này đều được sử dụng để đào tạo trong 2 chu kỳ, với kích thước mỗi lần xử lý là 1280 dữ liệu. Chúng tôi áp dụng thuật toán tối ưu hóa AdamW [23] kết hợp với lịch trình điều chỉnh tốc độ học máy loại cosine annealing [22], với tốc độ học máy được đặt ở mức 5e-5. Độ dài chuỗi dữ liệu được sử dụng để đào tạo là 4096.

---

**English:** <|ref|>title<|/ref|><|det|>[[117, 226, 368, 242]]<|/det|>
#### 3.5.2. Training DeepSeek-OCR  

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[117, 226, 368, 242]]<|/det|>
#### 3.5.2. Đào tạo DeepSeek-OCR

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 252, 881, 430]]<|/det|>
After DeepEncoder is ready, we use data mentioned in Section 3.4 to train the DeepSeek- OCR. with the entire training process conducted on the HAI- LLM [14] platform. The entire model uses pipeline parallelism (PP) and is divided into 4 parts, with DeepEncoder taking two parts and the decoder taking two parts. For DeepEncoder, we treat SAM and the compressor as the vision tokenizer, place them in PP0 and freeze their parameters, while treating the CLIP part as input embedding layer and place it in PP1 with unfrozen weights for training. For the language model part, since DeepSeek3B- MoE has 12 layers, we place 6 layers each on PP2 and PP3. We use 20 nodes (each with 8 A100- 40G GPUs) for training, with a data parallelism (DP) of 40 and a global batch size of 640. We use the AdamW optimizer with a step- based scheduler and an initial learning rate of 3e- 5. For text- only data, the training speed is 90B tokens/day, while for multimodal data, the training speed is 70B tokens/day.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 252, 881, 430]]<|/det|>  
Sau khi hoàn thành việc xây dựng công cụ DeepEncoder, chúng tôi sử dụng dữ liệu được đề cập ở Phần 3.4 để huấn luyện mô hình DeepSeek-OCR. Toàn bộ quá trình huấn luyện được thực hiện trên nền tảng HAI-LLM [14]. Mô hình này áp dụng phương pháp song song hóa dữ liệu và được chia thành 4 phần: DeepEncoder chiếm 2 phần, còn bộ giải mã chiếm 2 phần còn lại. Đối với phần DeepEncoder, chúng tôi coi các thành phần SAM và bộ nén dữ liệu như những công cụ xử lý văn bản, đặt chúng vào luồng xử lý PP0 và không thay đổi các tham số của chúng trong quá trình huấn luyện; trong khi đó, phần CLIP được xem là lớp đầu vào dùng để xử lý dữ liệu ngôn ngữ và được đặt vào luồng xử lý PP1, với các tham số có thể được điều chỉnh trong quá trình huấn luyện. Đối với phần mô hình ngôn ngữ, vì DeepSeek3B-MoE gồm 12 lớp, chúng tôi chia 6 lớp cho mỗi trong hai luồng xử lý PP2 và PP3. Chúng tôi sử dụng 20 node (mỗi node được trang bị 8 GPU loại A100-40G) để thực hiện quá trình huấn luyện, với mức độ song song hóa dữ liệu là 40 và kích thước mỗi lô dữ liệu là 640. Chúng tôi sử dụng thuật toán tối ưu hóa AdamW, kèm theo lịch trình huấn luyện dựa trên số bước và tỷ lệ học tập ban đầu là 3e-5. Đối với dữ liệu chỉ chứa văn bản, tốc độ huấn luyện là 90 tỷ token mỗi ngày; còn đối với dữ liệu đa phương thức, tốc độ huấn luyện là 70 tỷ token mỗi ngày.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 441, 881, 523]]<|/det|>
Table 2 | We test DeepSeek- OCR's vision- text compression ratio using all English documents with 600- 1300 tokens from the Fox [21] benchmarks. Text tokens represent the number of tokens after tokenizing the ground truth text using DeepSeek- OCR's tokenizer. Vision Tokens=64 or 100 respectively represent the number of vision tokens output by DeepEncoder after resizing input images to 512x512 and 640x640.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 441, 881, 523]]<|/det|>
Bảng 2: Chúng tôi đã kiểm tra tỷ lệ nén văn bản giữa hình ảnh và văn bản khi sử dụng công cụ DeepSeek-OCR, bằng cách sử dụng tất cả các tài liệu tiếng Anh có độ dài từ 600 đến 1300 ký tự trong bộ dữ liệu đánh giá của Fox [21]. Các ký tự văn bản được tính dựa trên số lượng ký tự sau khi văn bản gốc được phân tích bằng công cụ tokenizer của DeepSeek-OCR. Số lượng ký tự hình ảnh lần lượt là 64 hoặc 100, tùy thuộc vào việc hình ảnh đầu vào được điều chỉnh kích thước thành 512x512 hay 640x640 trước khi được xử lý bởi công cụ DeepEncoder.

---

**English:** <|ref|>table<|/ref|><|det|>[[211, 533, 784, 700]]<|/det|>

**Tiếng Việt:** <|ref|>bảng</|/ref|><|det|>[[211, 533, 784, 700]]</|/det|>

---

**English:** <table><tr><td rowspan="2">Text Tokens</td><td colspan="2">Vision Tokens =64</td><td colspan="2">Vision Tokens=100</td></tr><tr><td>Precision</td><td>Compression</td><td>Precision</td><td>Compression</td></tr><tr><td>600-700</td><td>96.5%</td><td>10.5×</td><td>98.5%</td><td>6.7×</td></tr><tr><td>700-800</td><td>93.8%</td><td>11.8×</td><td>97.3%</td><td>7.5×</td></tr><tr><td>800-900</td><td>83.8%</td><td>13.2×</td><td>96.8%</td><td>8.5×</td></tr><tr><td>900-1000</td><td>85.9%</td><td>15.1×</td><td>96.8%</td><td>9.7×</td></tr><tr><td>1000-1100</td><td>79.3%</td><td>16.5×</td><td>91.5%</td><td>10.6×</td></tr><tr><td>1100-1200</td><td>76.4%</td><td>17.7×</td><td>89.8%</td><td>11.3×</td></tr><tr><td>1200-1300</td><td>59.1%</td><td>19.7×</td><td>87.1%</td><td>12.6×</td></tr></table>  

**Tiếng Việt:** <table><tr><td rowspan="2">Các ký hiệu văn bản</td><td colspan="2">Số lượng ký hiệu hình ảnh = 64</td><td colspan="2">Số lượng ký hiệu hình ảnh = 100</td></tr><tr><td>Độ chính xác</td><td>Mức độ nén dữ liệu</td><td>Độ chính xác</td><td>Mức độ nén dữ liệu</td></tr><tr><td>600–700</td><td>96,5%</td><td>10,5 lần</td><td>98,5%</td><td>6,7 lần</td></tr><tr><td>700–800</td><td>93,8%</td><td>11,8 lần</td><td>97,3%</td><td>7,5 lần</td></tr><tr><td>800–900</td><td>83,8%</td><td>13,2 lần</td><td>96,8%</td><td>8,5 lần</td></tr><tr><td>900–1000</td><td>85,9%</td><td>15,1 lần</td><td>96,8%</td><td>9,7 lần</td></tr><tr><td>1000–1100</td><td>79,3%</td><td>16,5 lần</td><td>91,5%</td><td>10,6 lần</td></tr><tr><td>1100–1200</td><td>76,4%</td><td>17,7 lần</td><td>89,8%</td><td>11,3 lần</td></tr><tr><td>1200–1300</td><td>59,1%</td><td>19,7 lần</td><td>87,1%</td><td>12,6 lần</td></tr></table>

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 729, 253, 746]]<|/det|>
## 4. Evaluation  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 729, 253, 746]]<|/det|>
## 4. Đánh giá

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 761, 416, 777]]<|/det|>
### 4.1. Vision-text Compression Study  

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 761, 416, 777]]<|/det|>
### 4.1. Nghiên cứu về việc nén dữ liệu hình ảnh kết hợp văn bản

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 788, 881, 900]]<|/det|>
4. Evaluation4.1. Vision- text Compression StudyWe select Fox [21] benchmarks to verify DeepSeek- OCR's compression- decompression capability for text- rich documents, in order to preliminarily explore the feasibility and boundaries of contexts optical compression. We use the English document portion of Fox, tokenize the ground truth text with DeepSeek- OCR's tokenizer (vocabulary size of approximately 129k), and select documents with 600- 1300 tokens for testing, which happens to be 100 pages. Since the number of text tokens is not large, we only need to test performance in Tiny and Small modes, where Tiny mode corresponds to 64 tokens and Small mode corresponds to 100 tokens. We use the prompt

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 788, 881, 900]]<|/det|>  
4. Đánh giá  
4.1. Nghiên cứu về việc nén dữ liệu văn bản kết hợp hình ảnh  
Chúng tôi sử dụng các bài kiểm thử của Fox [21] để đánh giá khả năng nén và giải nén dữ liệu văn bản của công cụ DeepSeek-OCR, nhằm khám phá trước tiên tính khả thi và các hạn chế của phương pháp nén dữ liệu này. Chúng tôi lấy phần văn bản tiếng Anh trong tập dữ liệu Fox làm đối tượng thử nghiệm, tiến hành phân tích cấu trúc văn bản bằng công cụ tokenizer của DeepSeek-OCR (với bộ từ vựng gồm khoảng 129.000 từ), và chọn những tài liệu có số lượng từ từ 600 đến 1.300 để thử nghiệm – tương ứng với khoảng 100 trang văn bản. Vì số lượng từ trong các tài liệu này không quá lớn, chúng tôi chỉ cần kiểm tra hiệu suất của công cụ ở hai chế độ: “Tiny” (64 từ) và “Small” (100 từ). Chúng tôi sử dụng đoạn mã sau làm ví dụ để thực hiện thử nghiệm:

---

**English:** 
============================================================
--- Page 11 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 11 ---
============================================================

---

**English:** <|ref|>table<|/ref|><|det|>[[120, 207, 875, 707]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[115, 99, 881, 197]]<|/det|>
Table 3 | We use OmniDocBench [27] to test the performance of DeepSeek-OCR on real document parsing tasks. All metrics in the table are edit distances, where smaller values indicate better performance. "Tokens" represents the average number of vision tokens used per page, and \(\mathrm{^{i + 200dpi}}\) means using fitz to interpolate the original image to 200dpi. For the DeepSeek-OCR model, the values in parentheses in the "Tokens" column represent valid vision tokens, calculated according to Equation 1.   

**Tiếng Việt:** <|ref|>bảng</|/ref|><|det|>[[120, 207, 875, 707]]</|/det|>
<|ref|>chú thích bảng</|/ref|><|det|>[[115, 99, 881, 197]]</|/det|>
Bảng 3: Chúng tôi sử dụng công cụ OmniDocBench [27] để đánh giá hiệu suất của mô hình DeepSeek-OCR trong các tác vụ phân tích tài liệu thực tế. Tất cả các chỉ số trong bảng này đều là khoảng cách biên dịch; giá trị nhỏ hơn chứng tỏ hiệu suất tốt hơn. “Tokens” đại diện cho số lượng các ký hiệu được sử dụng trung bình trên mỗi trang; cụm “\(\mathrm{^{i + 200dpi}}\)” có nghĩa là sử dụng phương pháp Fitz để điều chỉnh độ phân giải hình ảnh gốc lên mức 200dpi. Đối với mô hình DeepSeek-OCR, các giá trị nằm trong ngoặc đơn ở cột “Tokens” là số lượng các ký hiệu hợp lệ được tính toán theo Phương trình 1.

---

**English:** <table><tr><td rowspan="2">Model</td><td rowspan="2">Tokens</td><td colspan="4">English</td><td colspan="4">Chinese</td></tr><tr><td>overall</td><td>text</td><td>formula</td><td>table</td><td>order</td><td>overall</td><td>text</td><td>formula</td></tr><tr><td colspan="10">Pipline Models</td></tr><tr><td>Dolphin [11]</td><td>-</td><td>0.356</td><td>0.352</td><td>0.465</td><td>0.258</td><td>0.35</td><td>0.44</td><td>0.44</td><td>0.604</td></tr><tr><td>Marker [1]</td><td>-</td><td>0.296</td><td>0.085</td><td>0.374</td><td>0.609</td><td>0.116</td><td>0.497</td><td>0.293</td><td>0.688</td></tr><tr><td>Mathpix [2]</td><td>-</td><td>0.191</td><td>0.105</td><td>0.306</td><td>0.243</td><td>0.108</td><td>0.364</td><td>0.381</td><td>0.454</td></tr><tr><td>MinerU-2.1.1 [34]</td><td>-</td><td>0.162</td><td>0.072</td><td>0.313</td><td>0.166</td><td>0.097</td><td>0.244</td><td>0.111</td><td>0.581</td></tr><tr><td>MonkeyOCR-1.2B [18]</td><td>-</td><td>0.154</td><td>0.062</td><td>0.295</td><td>0.164</td><td>0.094</td><td>0.263</td><td>0.179</td><td>0.464</td></tr><tr><td>PPstructure-v3 [9]</td><td>-</td><td>0.152</td><td>0.073</td><td>0.295</td><td>0.162</td><td>0.077</td><td>0.223</td><td>0.136</td><td>0.535</td></tr><tr><td colspan="10">End-to-end Models</td></tr><tr><td>Nougat [6]</td><td>2352</td><td>0.452</td><td>0.365</td><td>0.488</td><td>0.572</td><td>0.382</td><td>0.973</td><td>0.998</td><td>0.941</td></tr><tr><td>SmolDocking [25]</td><td>392</td><td>0.493</td><td>0.262</td><td>0.753</td><td>0.729</td><td>0.227</td><td>0.816</td><td>0.838</td><td>0.997</td></tr><tr><td>InternVL2-76B [8]</td><td>6790</td><td>0.44</td><td>0.353</td><td>0.543</td><td>0.547</td><td>0.317</td><td>0.443</td><td>0.29</td><td>0.701</td></tr><tr><td>Qwen2.5-VL-7B [5]</td><td>3949</td><td>0.316</td><td>0.151</td><td>0.376</td><td>0.598</td><td>0.138</td><td>0.399</td><td>0.243</td><td>0.5</td></tr><tr><td>OLMOCR [28]</td><td>3949</td><td>0.326</td><td>0.097</td><td>0.455</td><td>0.608</td><td>0.145</td><td>0.469</td><td>0.293</td><td>0.655</td></tr><tr><td>GOT-OCR2.0 [38]</td><td>256</td><td>0.287</td><td>0.189</td><td>0.360</td><td>0.459</td><td>0.141</td><td>0.411</td><td>0.315</td><td>0.528</td></tr><tr><td>OCRFlux-3B [3]</td><td>3949</td><td>0.238</td><td>0.112</td><td>0.447</td><td>0.269</td><td>0.126</td><td>0.349</td><td>0.256</td><td>0.716</td></tr><tr><td>GPT4o [26]</td><td>-</td><td>0.233</td><td>0.144</td><td>0.425</td><td>0.234</td><td>0.128</td><td>0.399</td><td>0.409</td><td>0.606</td></tr><tr><td>InternVL3-78B [42]</td><td>6790</td><td>0.218</td><td>0.117</td><td>0.38</td><td>0.279</td><td>0.095</td><td>0.296</td><td>0.21</td><td>0.533</td></tr><tr><td>Qwen2.5-VL-72B [5]</td><td>3949</td><td>0.214</td><td>0.092</td><td>0.315</td><td>0.341</td><td>0.106</td><td>0.261</td><td>0.18</td><td>0.434</td></tr><tr><td>dots.ocr [30]</td><td>3949</td><td>0.182</td><td>0.137</td><td>0.320</td><td>0.166</td><td>0.182</td><td>0.261</td><td>0.229</td><td>0.468</td></tr><tr><td>Gemini2.5-Pro [4]</td><td>-</td><td>0.148</td><td>0.055</td><td>0.356</td><td>0.13</td><td>0.049</td><td>0.212</td><td>0.168</td><td>0.439</td></tr><tr><td>MinerU2.0 [34]</td><td>6790</td><td>0.133</td><td>0.045</td><td>0.273</td><td>0.15</td><td>0.066</td><td>0.238</td><td>0.115</td><td>0.506</td></tr><tr><td>dots.ocr+200dpi [30]</td><td>5545</td><td>0.125</td><td>0.032</td><td>0.329</td><td>0.099</td><td>0.04</td><td>0.16</td><td>0.066</td><td>0.416</td></tr><tr><td colspan="10">DeepSeek-OCR (end2end)</td></tr><tr><td>Tiny</td><td>64</td><td>0.386</td><td>0.373</td><td>0.469</td><td>0.422</td><td>0.283</td><td>0.361</td><td>0.307</td><td>0.635</td></tr><tr><td>Small</td><td>100</td><td>0.221</td><td>0.142</td><td>0.373</td><td>0.242</td><td>0.125</td><td>0.284</td><td>0.24</td><td>0.53</td></tr><tr><td>Base</td><td>256(182)</td><td>0.137</td><td>0.054</td><td>0.267</td><td>0.163</td><td>0.064</td><td>0.24</td><td>0.205</td><td>0.474</td></tr><tr><td>Large</td><td>400(285)</td><td>0.138</td><td>0.054</td><td>0.277</td><td>0.152</td><td>0.067</td><td>0.208</td><td>0.143</td><td>0.461</td></tr><tr><td>Gundam</td><td>795</td><td>0.127</td><td>0.043</td><td>0.269</td><td>0.134</td><td>0.062</td><td>0.181</td><td>0.097</td><td>0.432</td></tr><tr><td>Gundam-M+200dpi</td><td>1853</td><td>0.123</td><td>0.049</td><td>0.242</td><td>0.147</td><td>0.056</td><td>0.157</td><td>0.087</td><td>0.377</td></tr></table>  

**Tiếng Việt:** **Bảng so sánh các mô hình nhận dạng văn bản**  

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 727, 880, 775]]<|/det|>
without layout: "&lt;image&gt;\nFree OCR." to control the model's output format. Nevertheless, the output format still cannot completely match Fox benchmarks, so the actual performance would be somewhat higher than the test results.  

**Tiếng Việt:** | **Mô hình**          | **Số lượng token được sử dụng** | **Điểm đánh giá tiếng Anh** | **Điểm đánh giá tiếng Trung** |
|-------------------|---------------------------------|-------------------|-------------------------|
| **Dolphin [11]**      | -                           | 0.356              | 0.352                    |
| **Marker [1]**       | -                           | 0.296              | 0.085                    |
| **Mathpix [2]**      | -                           | 0.191              | 0.105                    |
| **MinerU-2.1.1 [34]** | -                           | 0.162              | 0.072                    |
| **MonkeyOCR-1.2B [18]** | -                           | 0.154              | 0.062                    |
| **PPstructure-v3 [9]** | -                           | 0.152              | 0.073                    |
| **Nougat [6]**        | 2352                        | 0.452              | 0.365                    |
| **SmolDocking [25]**    | 392                         | 0.493              | 0.262                    |
| **InternVL2-76B [8]** | 6790                        | 0.44               | 0.353                    |
| **Qwen2.5-VL-7B [5]** | 3949                        | 0.316              | 0.151                    |
| **OLMOCR [28]**      | 3949                        | 0.326              | 0.097                    |
| **GOT-OCR2.0 [38]**     | 256                         | 0.287              | 0.189                    |
| **OCRFlux-3B [3]**     | 3949                        | 0.238              | 0.112                    |
| **GPT4o [26]**       | -                           | 0.233              | 0.144                    |
| **InternVL3-78B [42]** | 6790                        | 0.218              | 0.117                    |
| **Qwen2.5-VL-72B [5]** | 3949                        | 0.214              | 0.092                    |
| **dots.ocr [30]**     | 3949                        | 0.182              | 0.137                    |
| **Gemini2.5-Pro [4]**   | -                           | 0.148              | 0.055                    |
| **MinerU2.0 [34]**     | 6790                        | 0.133              | 0.045                    |
| **dots.ocr+200dpi [30]** | 5545                        | 0.125              | 0.032                    |
| **DeepSeek-OCR (end2end)** | <colspan="2">Các cấp độ khác nhau</colspan> | <colspan="2">Các cấp độ khác nhau</colspan> | <colspan="2">Các cấp độ khác nhau</colspan> |

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 783, 881, 897]]<|/det|>
As shown in Table 2, within a \(10\times\) compression ratio, the model's decoding precision can reach approximately \(97\%\) , which is a very promising result. In the future, it may be possible to achieve nearly \(10\times\) lossless contexts compression through text- to- image approaches. When the compression ratio exceeds \(10\times\) , performance begins to decline, which may have two reasons: one is that the layout of long documents becomes more complex, and another reason may be that long texts become blurred at \(512\times 512\) or \(640\times 640\) resolution. The first issue can be solved by rendering texts onto a single layout page, while we believe the second issue will become

**Tiếng Việt:** **Lưu ý:** Các chỉ số đánh giá được tính dựa trên nhiều yếu tố, bao gồm hiệu suất nhận diện văn bản, tốc độ xử lý, độ chính xác, v.v. Các con số trong bảng thể hiện thứ hạng của từng mô hình so với các mô hình khác trong cùng nhóm.

---

**English:** 
============================================================
--- Page 12 ---
============================================================

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 727, 880, 775]]<|/det|>  
Nếu không sử dụng bố cục đặc biệt, có thể sử dụng dòng “<image>\nFree OCR.” để điều khiển định dạng đầu ra của mô hình. Tuy nhiên, định dạng đầu ra này vẫn chưa thể hoàn toàn tương thích với các tiêu chuẩn đánh giá của Fox; do đó, hiệu suất thực tế có thể cao hơn một chút so với kết quả đo lường.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 100, 881, 180]]<|/det|>
a feature of the forgetting mechanism. When compressing tokens by nearly \(20\times\) , we find that precision can still approach \(60\%\) . These results indicate that optical contexts compression is a very promising and worthwhile research direction, and this approach does not bring any overhead because it can leverage VLM infrastructure, as multimodal systems inherently require an additional vision encoder.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 783, 881, 897]]<|/det|>
As shown in Table 2, within a \(10\times\) compression ratio, the model's decoding precision can reach approximately \(97\%\), which is a very promising result. In the future, it may be possible to achieve nearly \(10\times\) lossless contexts compression through text- to- image approaches. When the compression ratio exceeds \(10\times\), performance begins to decline, which may have two reasons: one is that the layout of long documents becomes more complex, and another reason may be that long texts become blurred at \(512\times 512\) or \(640\times 640\) resolution. The first issue can be solved by rendering texts onto a single layout page, while we believe the second issue will become<|ref|>text<|/ref|><|det|>[[115, 783, 881, 897]]<|/det|>  
Như được thể hiện trong Bảng 2, với tỷ lệ nén là 10 lần, độ chính xác khi giải mã dữ liệu bằng mô hình này có thể đạt khoảng 97%, đây là một kết quả rất đáng khích lệ. Trong tương lai, có thể sẽ có thể thực hiện được việc nén dữ liệu mà không làm mất thông tin với tỷ lệ gần 10 lần thông qua các phương pháp chuyển đổi văn bản thành hình ảnh. Tuy nhiên, khi tỷ lệ nén vượt quá 10 lần, hiệu suất của mô hình bắt đầu giảm sút; điều này có thể xuất phát từ hai lý do: thứ nhất là cấu trúc trang trình bày của các văn bản dài trở nên phức tạp hơn; thứ hai là các đoạn văn bản dài có thể bị mờ đi khi được hiển thị ở độ phân giải 512×512 hoặc 640×640. Vấn đề thứ nhất có thể được giải quyết bằng cách hiển thị toàn bộ nội dung văn bản trên cùng một trang, trong khi chúng tôi tin rằng vấn đề thứ hai cũng sẽ được khắc phục theo thời gian.

---

**English:** <|ref|>table_caption<|/ref|><|det|>[[115, 192, 881, 238]]<|/det|>
Table 4 | Edit distances for different categories of documents in OmniDocBench. The results show that some types of documents can achieve good performance with just 64 or 100 vision tokens, while others require Gundam mode.

**Tiếng Việt:** ============================================================
--- Trang 12 ---
============================================================

---

**English:** <|ref|>table<|/ref|><|det|>[[128, 250, 870, 380]]<|/det|>

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 100, 881, 180]]<|/det|>
a feature of the forgetting mechanism. When compressing tokens by nearly \(20\times\), we find that precision can still approach \(60\%\). These results indicate that optical contexts compression is a very promising and worthwhile research direction, and this approach does not bring any overhead because it can leverage VLM infrastructure, as multimodal systems inherently require an additional vision encoder.<|ref|>text<|/ref|><|det|>[[115, 100, 881, 180]]<|/det|>  
Đây là một đặc điểm nổi bật của cơ chế quên lãng. Khi nén các dữ liệu này gần như \(20\times\), chúng ta vẫn có thể đạt được độ chính xác lên tới khoảng \(60\%\). Những kết quả này cho thấy rằng việc nén thông tin liên quan đến ngữ cảnh hình ảnh là một hướng nghiên cứu rất triển vọng và đáng giá; đồng thời, phương pháp này không gây ra bất kỳ gánh nặng nào vì nó có thể tận dụng trực tiếp cơ sở hạ tầng của các hệ thống VLM, trong khi các hệ thống đa phương thức vốn đã cần đến các bộ mã hóa hình ảnh bổ sung.

---

**English:** <table><tr><td>Type<br>Mode</td><td>Book Slides</td><td>Financial<br>Report</td><td>Textbook</td><td>Exam<br>Paper</td><td>Magazine</td><td>Academic<br>Papers</td><td>Notes</td><td>Newspaper Overall</td></tr><tr><td>Tiny</td><td>0.147 0.116</td><td>0.207</td><td>0.173</td><td>0.294</td><td>0.201</td><td>0.395</td><td>0.297</td><td>0.94</td></tr><tr><td>Small</td><td>0.085 0.111</td><td>0.079</td><td>0.147</td><td>0.171</td><td>0.107</td><td>0.131</td><td>0.187</td><td>0.744</td></tr><tr><td>Base</td><td>0.037 0.08</td><td>0.027</td><td>0.1</td><td>0.13</td><td>0.073</td><td>0.052</td><td>0.176</td><td>0.645</td></tr><tr><td>Large</td><td>0.038 0.108</td><td>0.022</td><td>0.084</td><td>0.109</td><td>0.06</td><td>0.053</td><td>0.155</td><td>0.353</td></tr><tr><td>Gundam</td><td>0.035 0.085</td><td>0.289</td><td>0.095</td><td>0.094</td><td>0.059</td><td>0.039</td><td>0.153</td><td>0.122</td></tr><tr><td>Guandam-M</td><td>0.052 0.09</td><td>0.034</td><td>0.091</td><td>0.079</td><td>0.079</td><td>0.048</td><td>0.1</td><td>0.099</td></tr></table>

**Tiếng Việt:** <|ref|>table_caption<|/ref|><|det|>[[115, 192, 881, 238]]<|/det|>
Bảng 4 | Khoảng cách cần thiết để chỉnh sửa các loại tài liệu khác nhau trong OmniDocBench. Kết quả cho thấy một số loại tài liệu có thể đạt được hiệu suất tốt chỉ với 64 hoặc 100 “token” hình ảnh, trong khi những loại khác lại yêu cầu phải sử dụng chế độ “Gundam”.

---

**English:** <|ref|>title<|/ref|><|det|>[[115, 414, 385, 426]]<|/det|>
# 4.2. OCR Practical Performance

**Tiếng Việt:** <|ref|>bảng</|/ref|><|det|>[[128, 250, 870, 380]]</|/det|>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 440, 883, 583]]<|/det|>
DeepSeek-OCR is not only an experimental model; it has strong practical capabilities and can construct data for LLM/VLM pretraining. To quantify OCR performance, we test DeepSeek-OCR on OmniDocBench [27], with results shown in Table 3. Requiring only 100 vision tokens (640x640 resolution), DeepSeek-OCR surpasses GOT-OCR2.0 [38] which uses 256 tokens; with 400 tokens (285 valid tokens, 1280x1280 resolution), it achieves on-par performance with state-of-the-arts on this benchmark. Using fewer than 800 tokens (Gundam mode), DeepSeek-OCR outperforms MinerU2.0 [34] which needs nearly 7,000 vision tokens. These results demonstrate that our DeepSeek-OCR model is powerful in practical applications, and because the higher tokens compression, it enjoys a higher research ceiling.

**Tiếng Việt:** <table><tr><td>Loại<br>Mức độ phân giải</td><td>Trang trình bày sách</td><td>Báo cáo tài chính</td><td>Sách giáo khoa</td><td>Bài thi</td><td>Tạp chí</td><>Luận văn học thuật</td><>Ghi chú</td><>Báo chí tổng thể</td></tr><tr><td>Cực nhỏ</td><td>0.147 0.116</td><td>0.207</td><td>0.173</td><td>0.294</td><td>0.201</td><td>0.395</td><td>0.297</td><td>0.94</td></tr><tr><td>Nhỏ</td><td>0.085 0.111</td><td>0.079</td><td>0.147</td><td>0.171</td><td>0.107</td><td>0.131</td><td>0.187</td><td>0.744</td></tr><tr><td>Trung bình</td><td>0.037 0.08</td><td>0.027</td><td>0.1</td><td>0.13</td><td>0.073</td><td>0.052</td><td>0.176</td><td>0.645</td></tr><tr><td>Lớn</td><td>0.038 0.108</td><td>0.022</td><td>0.084</td><td>0.109</td><td>0.06</td><td>0.053</td><td>0.155</td><td>0.353</td></tr><tr><td>Gundam</td><td>0.035 0.085</td><td>0.289</td><td>0.095</td><td>0.094</td><td>0.059</td><td>0.039</td><td>0.153</td><td>0.122</td></tr><tr><td>Guandam-M</td><td>0.052 0.09</td><td>0.034</td><td>0.091</td><td>0.079</td><td>0.079</td><td>0.048</td><td>0.1</td><td>0.099</td></tr></table>

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 594, 883, 752]]<|/det|>
As shown in Table 4, some categories of documents require very few tokens to achieve satisfactory performance, such as slides which only need 64 vision tokens. For book and report documents, DeepSeek-OCR can achieve good performance with only 100 vision tokens.Combined with the analysis from Section 4.1, this may be because most text tokens in these document categories are within 1,000, meaning the vision-token compression ratio does not exceed 10x. For newspapers, Gundam or even Gundam-master mode is required to achieve acceptable edit distances, because the text tokens in newspapers are 4-5,000, far exceeding the 10x compression of other modes. These experimental results further demonstrate the boundaries of contexts optical compression, which may provide effective references for researches on the vision token optimization in VLMs and context compression, forgetting mechanisms in LLMs.

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[115, 414, 385, 426]]<|/det|>
# 4.2. Hiệu suất thực tế của công nghệ OCR

---

**English:** <|ref|>title<|/ref|><|det|>[[115, 778, 306, 790]]<|/det|>
# 4.3. Qualitative Study

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 440, 883, 583]]<|/det|>  
DeepSeek-OCR không chỉ là một mô hình thử nghiệm mà còn sở hữu khả năng ứng dụng thực tế mạnh mẽ, đồng thời có thể được sử dụng để xây dựng dữ liệu phục vụ việc huấn luyện các mô hình LLM/VLM. Để đánh giá hiệu suất của DeepSeek-OCR, chúng tôi đã thử nghiệm nó trên bộ dữ liệu OmniDocBench [27]; kết quả được trình bày trong Bảng 3. Chỉ cần sử dụng 100 “token hình ảnh” (với độ phân giải 640x640), DeepSeek-OCR đã vượt trội hơn so với GOT-OCR2.0 [38] – mô hình yêu cầu sử dụng tới 256 token hình ảnh. Khi sử dụng 400 token hình ảnh (trong đó 285 token hữu ích, độ phân giải 1280x1280), DeepSeek-OCR đạt được hiệu suất ngang ngửa với các mô hình tiên tiến nhất trên bài kiểm thử này. Với lượng token hình ảnh ít hơn 800 (chế độ sử dụng “Gundam”), DeepSeek-OCR còn vượt trội hơn so với MinerU2.0 [34] – mô hình cần tới gần 7.000 token hình ảnh. Những kết quả này chứng minh rằng mô hình DeepSeek-OCR của chúng tôi rất mạnh mẽ trong các ứng dụng thực tế; đồng thời, nhờ khả năng nén dữ liệu hiệu quả, mô hình này còn tiềm năng phát triển cao hơn nữa trong lĩnh vực nghiên cứu khoa học.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 804, 278, 817]]<|/det|>
## 4.3.1. Deep parsing

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 594, 883, 752]]<|/det|>  
Như được thể hiện trong Bảng 4, một số loại tài liệu chỉ cần rất ít các “token văn bản” là đã đạt được hiệu suất xử lý đáng mong đợi; ví dụ, các trang trình bày chỉ cần 64 “token văn bản” là đủ. Đối với các tài liệu sách hoặc báo cáo, phương pháp DeepSeek-OCR cũng có thể hoạt động hiệu quả với chỉ 100 “token văn bản”. Kết hợp với kết quả phân tích ở Phần 4.1, điều này có thể được giải thích do hầu hết các “token văn bản” trong những loại tài liệu này đều nằm trong khoảng từ 1.000 đến 5.000, nên tỷ lệ nén chúng không vượt quá 10 lần. Trong khi đó, đối với các tài liệu báo chí hoặc nội dung liên quan đến Gundam, cần sử dụng các chế độ nén chuyên biệt (như chế độ Gundam hay Gundam-Master) mới có thể đạt được độ chính xác xử lý đủ cao; bởi vì số lượng “token văn bản” trong những loại tài liệu này lên đến 4.000 đến 5.000, vượt xa mức 10 lần nén mà các chế độ khác có thể đạt được. Những kết quả thí nghiệm này càng làm rõ các giới hạn của phương pháp nén văn bản dựa trên ngữ cảnh, đồng thời cung cấp những thông tin hữu ích cho các nghiên cứu về việc tối ưu hóa cách thức xử lý “token văn bản” trong các hệ thống trí tuệ nhân tạo, cũng như các phương pháp nén dữ liệu dựa trên ngữ cảnh hoặc cơ chế “quên” thông tin trong các mô hình trí tuệ nhân tạo lớn.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 830, 883, 891]]<|/det|>
DeepSeek-OCR possesses both layout and OCR 2.0 capabilities, enabling it to further parse images within documents through secondary model calls, a feature we refer to as "deep parsing".As shown in Figures 7,8,9,10, our model can perform deep parsing on charts, geometry, chemical formulas, and even natural images, requiring only a unified prompt.

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[115, 778, 306, 790]]<|/det|>
# 4.3. Nghiên cứu định tính

---

**English:** 
============================================================
--- Page 13 ---
============================================================

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 804, 278, 817]]<|/det|>
## 4.3.1. Phân tích sâu</td>

---

**English:** ![Image 0_0](images/page_13_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 810, 881, 875]]<|/det|>
<center>Figure 7 | In the field of financial research reports, the deep parsing mode of DeepSeek-OCR can be used to obtain structured results of charts within documents. Charts are a crucial form of data representation in finance and scientific fields, and the chart structured extraction is an indispensable capability for future OCR models. </center>

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 830, 883, 891]]<|/det|>  
DeepSeek-OCR vừa sở hữu khả năng phân tích cấu trúc trang văn bản, vừa có thể thực hiện các thao tác nhận dạng ký tự quang học theo tiêu chuẩn OCR 2.0; điều này cho phép mô hình của chúng tôi tiếp tục phân tích các hình ảnh trong tài liệu thông qua việc gọi lại các mô hình phụ trợ, và chúng tôi gọi tính năng này là “phân tích sâu”. Như được minh họa trong Hình 7, 8, 9 và 10, mô hình của chúng tôi có thể thực hiện các thao tác phân tích sâu trên các biểu đồ, công thức hóa học, thậm chí cả các hình ảnh thông thường, và chỉ cần một yêu cầu đầu vào thống nhất là đủ.

---

**English:** 
============================================================
--- Page 14 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 13 ---
============================================================

---

**English:** ![Image 0_0](images/page_14_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[258, 465, 340, 477]]<|/det|>
<center>Input image </center>  

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_13_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 810, 881, 875]]<|/thông tin chi tiết|>
<center>Hình 7 | Trong lĩnh vực báo cáo nghiên cứu tài chính, chế độ phân tích sâu của công cụ DeepSeek-OCR có thể được sử dụng để trích xuất các biểu đồ có cấu trúc rõ ràng từ các tài liệu. Biểu đồ là hình thức biểu diễn dữ liệu quan trọng trong lĩnh vực tài chính và khoa học; do đó, khả năng trích xuất thông tin từ các biểu đồ một cách có cấu trúc là yếu tố thiết yếu đối với các mô hình OCR trong tương lai.</center>

---

**English:** ![Image 1_0](images/page_14_img_1_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[668, 460, 714, 472]]<|/det|>
<center>Result </center>  

**Tiếng Việt:** ============================================================
--- Trang 14 ---
============================================================

---

**English:** ![Image 2_0](images/page_14_img_2_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 818, 881, 867]]<|/det|>
<center>Figure 8 | For books and articles, the deep parsing mode can output dense captions for natural images in the documents. With just a prompt, the model can automatically identify what type of image it is and output the required results. </center>

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_14_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin|>[[258, 465, 340, 477]]<|/thông tin|>
<center>Hình ảnh đầu vào</center>

---

**English:** 
============================================================
--- Page 15 ---
============================================================

**Tiếng Việt:** ![Hình ảnh 1_0](images/page_14_img_1_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[668, 460, 714, 472]]<|/thông tin chi tiết|>
<center>Kết quả</center>

---

**English:** ![Image 0_0](images/page_15_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[114, 817, 881, 866]]<|/det|>
<center>Figure 9 | DeepSeek-OCR in deep parsing mode can also recognize chemical formulas within chemical documents and convert them to SMILES format. In the future, OCR 1.0+2.0 technology may play a significant role in the development of VLM/LLM in STEM fields. </center>

**Tiếng Việt:** ![Hình 2_0](images/page_14_img_2_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 818, 881, 867]]<|/thông tin chi tiết|>
<center>Hình 8: Đối với sách và bài viết, chế độ phân tích sâu có thể tạo ra các chú thích chi tiết cho các hình ảnh trong tài liệu. Chỉ cần một yêu cầu nhỏ, mô hình có thể tự động xác định loại hình ảnh đó và hiển thị kết quả cần thiết.</center>

---

**English:** 
============================================================
--- Page 16 ---
============================================================

**Tiếng Việt:** ============================================================
--- Trang 15 ---
============================================================

---

**English:** ![Image 0_0](images/page_16_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 722, 881, 772]]<|/det|>
<center>Figure 10 | DeepSeek-OCR also possesses the capability to copy (structure) simple planar geometric figures. Due to the intricate interdependencies among line segments in geometric shapes, parsing geometry task is extremely challenging and has a long way to go. </center>  

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_15_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[114, 817, 881, 866]]<|/thông tin chi tiết|>
<center>Hình 9: Chức năng nhận dạng văn bản bằng công nghệ OCR của DeepSeek-OCR, khi hoạt động ở chế độ phân tích sâu, cũng có thể nhận diện được các công thức hóa học trong các tài liệu khoa học và chuyển chúng sang định dạng SMILES. Trong tương lai, công nghệ OCR phiên bản 1.0 và 2.0 có thể đóng vai trò quan trọng trong sự phát triển của các mô hình trí tuệ nhân tạo dùng cho lĩnh vực Khoa học, Công nghệ, Kỹ thuật và Toán học.</center>

---

**English:** <|ref|>title<|/ref|><|det|>[[117, 794, 371, 810]]<|/det|>
#### 4.3.2. Multilingual recognition  

**Tiếng Việt:** ============================================================
--- Trang 16 ---
============================================================

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 820, 883, 902]]<|/det|>
PDF data on the Internet contains not only Chinese and English, but also a large amount of multilingual data, which is also crucial when training LLMs. For PDF documents, DeepSeek- OCR can handle nearly 100 languages. Like Chinese and English documents, multilingual data also supports both layout and non- layout OCR formats. The visualization results are shown in Figure 11, where we select Arabic and Sinhala languages to demonstrate results.

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_16_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 722, 881, 772]]<|/thông tin chi tiết|>
<center>Hình 10 | DeepSeek-OCR cũng có khả năng sao chép các hình dạng hình học đơn giản. Do mối quan hệ phức tạp giữa các đoạn thẳng trong các hình học này, việc phân tích chúng là một nhiệm vụ vô cùng thách thức và còn nhiều công việc phải làm trước khi đạt được kết quả mong muốn.</center>

---

**English:** 
============================================================
--- Page 17 ---
============================================================

**Tiếng Việt:** <|ref|>title<|/ref|><|det|>[[117, 794, 371, 810]]<|/det|>
#### 4.3.2. Nhận dạng ngôn ngữ đa dạng

---

**English:** ![Image 0_0](images/page_17_img_0_0.jpg)
 

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 820, 883, 902]]<|/det|>  
Các tài liệu PDF trên mạng Internet không chỉ chứa ngôn ngữ Trung Quốc và Anh, mà còn bao gồm rất nhiều dữ liệu đa ngôn ngữ; những dữ liệu này cũng đóng vai trò quan trọng trong quá trình huấn luyện các mô hình LLM. Đối với các tài liệu PDF, công cụ DeepSeek-OCR có thể xử lý gần 100 ngôn ngữ khác nhau. Giống như các tài liệu tiếng Trung và tiếng Anh, dữ liệu đa ngôn ngữ cũng được hỗ trợ trong cả các định dạng OCR có cấu trúc và không có cấu trúc. Kết quả đồ họa được trình bày trong Hình 11; chúng tôi đã chọn hai ngôn ngữ là tiếng Ả Rập và tiếng Sinhala để minh họa các kết quả này.

---

**English:** <|ref|>image_caption<|/ref|><|det|>[[113, 789, 880, 839]]<|/det|>
<center>Figure 11 | To endow the capability of processing widely crawled PDFs (multilingual data), we train our model with OCR capabilities for nearly 100 languages. Minority language documents can also support both layout and non-layout outputs through different prompts.</center> 

**Tiếng Việt:** ============================================================
--- Trang 17 ---
============================================================

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[113, 860, 415, 877]]<|/det|>
## 4.3.3. General vision understanding 

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_17_img_0_0.jpg)

---

**English:** <|ref|>text<|/ref|><|det|>[[113, 888, 880, 920]]<|/det|>
We also provide DeepSeek-OCR with a certain degree of general image understanding capabilities. The related visualization results are shown in Figure 12.

**Tiếng Việt:** <|ref|>image_caption<|/ref|><|det|>[[113, 789, 880, 839]]<|/det|>
<center>Hình 11: Để cho mô hình có khả năng xử lý các tệp PDF được thu thập từ nhiều nguồn khác nhau (dữ liệu đa ngôn ngữ), chúng tôi đã huấn luyện mô hình này với các công nghệ nhận dạng chữ viết quang học (OCR) dành cho gần 100 ngôn ngữ. Các tài liệu bằng ngôn ngữ thiểu số cũng có thể được xử lý thành cả dạng có cấu trúc trang trí và dạng không có cấu trúc trang trí, tùy thuộc vào các thông tin đầu vào được sử dụng.</center>

---

**English:** 
============================================================
--- Page 18 ---
============================================================

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[113, 860, 415, 877]]<|/det|>
## 4.3.3. Hiểu biết tổng quát về hình ảnh

---

**English:** ![Image 0_0](images/page_18_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 660, 883, 743]]<|/det|>
<center>Figure 12 | We retain DeepSeek-OCR's capabilities in general visual understanding, mainly including image description, object detection, grounding, etc. Meanwhile, due to the inclusion of text-only data, DeepSeek-OCR's language capabilities are also retained. Note that since we do not include SFT (Supervised Fine-Tuning) stage, the model is not a chatbot, and some capabilities need completion prompts to be activated. </center>  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[113, 888, 880, 920]]<|/det|>  
Chúng tôi cũng trang bị cho DeepSeek-OCR những khả năng nhất định trong việc hiểu biết về các hình ảnh nói chung. Kết quả minh họa liên quan được trình bày trong Hình 12.

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[117, 766, 255, 784]]<|/det|>
## 5. Discussion  

**Tiếng Việt:** ============================================================
--- Trang 18 ---
============================================================

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 797, 883, 895]]<|/det|>
Our work represents an initial exploration into the boundaries of vision-text compression, investigating how many vision tokens are required to decode \(N\) text tokens. The preliminary results are encouraging: DeepSeek- OCR achieves near- lossless OCR compression at approximately \(10 \times\) ratios, while \(20 \times\) compression still retains \(60\%\) accuracy. These findings suggest promising directions for future applications, such as implementing optical processing for dialogue histories beyond \(k\) rounds in multi- turn conversations to achieve \(10 \times\) compression efficiency.

**Tiếng Việt:** ![Hình 0_0](images/page_18_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 660, 883, 743]]<|/thông tin chi tiết|>
<center>Hình 12: Mô hình DeepSeek-OCR vẫn giữ được các khả năng liên quan đến việc hiểu biết hình ảnh nói chung, bao gồm mô tả hình ảnh, phát hiện đối tượng, xác định vị trí đối tượng trong hình, v.v. Đồng thời, nhờ việc sử dụng dữ liệu chỉ chứa văn bản, khả năng xử lý ngôn ngữ của DeepSeek-OCR cũng được duy trì. Lưu ý rằng vì chúng tôi không áp dụng giai đoạn huấn luyện có giám sát (SFT), nên mô hình này không phải là một bot trò chuyện; một số chức năng chỉ có thể được kích hoạt khi có yêu cầu cụ thể từ người dùng.</center>

---

**English:** 
============================================================
--- Page 19 ---
============================================================

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[117, 766, 255, 784]]<|/det|>
## 5. Thảo luận

---

**English:** ![Image 0_0](images/page_19_img_0_0.jpg)
<|ref|>image_caption<|/ref|><|det|>[[115, 279, 883, 360]]<|/det|>
<center>Figure 13 | Forgetting mechanisms constitute one of the most fundamental characteristics of human memory. The contexts optical compression approach can simulate this mechanism by rendering previous rounds of historical text onto images for initial compression, then progressively resizing older images to achieve multi-level compression, where token counts gradually decrease and text becomes increasingly blurred, thereby accomplishing textual forgetting. </center>  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 797, 883, 895]]<|/det|>  
Công trình nghiên cứu của chúng tôi đại diện cho những khám phá ban đầu về các giới hạn trong việc nén dữ liệu hình ảnh kết hợp văn bản; chúng tôi đã tìm hiểu xem cần bao nhiêu thông tin hình ảnh là đủ để giải mã một số lượng nhất định thông tin văn bản. Kết quả ban đầu rất đáng khích lệ: Phương pháp DeepSeek-OCR cho phép thực hiện việc nén dữ liệu gần như không mất thông tin, với tỷ lệ nén khoảng 10 lần; ngay cả khi tỷ lệ nén lên đến 20 lần, độ chính xác trong việc giải mã vẫn đạt mức 60%. Những phát hiện này mở ra những hướng đi hứa hẹn cho các ứng dụng tương lai, chẳng hạn như việc áp dụng các công nghệ xử lý hình ảnh trong các cuộc đối thoại có nhiều vòng, nhằm đạt được hiệu quả nén lên đến 10 lần.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 384, 881, 499]]<|/det|>
For older contexts, we could progressively downsizing the rendered images to further reduce token consumption. This assumption draws inspiration from the natural parallel between human memory decay over time and visual perception degradation over spatial distance—both exhibit similar patterns of progressive information loss, as shown in Figure 13. By combining these mechanisms, contexts optical compression method enables a form of memory decay that mirrors biological forgetting curves, where recent information maintains high fidelity while distant memories naturally fade through increased compression ratios.  

**Tiếng Việt:** ============================================================
--- Trang 19 ---
============================================================

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 505, 882, 603]]<|/det|>
While our initial exploration shows potential for scalable ultra- long context processing, where recent contexts preserve high resolution and older contexts consume fewer resources, we acknowledge this is early- stage work that requires further investigation. The approach suggests a path toward theoretically unlimited context architectures that balance information retention with computational constraints, though the practical implications and limitations of such vision- text compression systems warrant deeper study in future research.  

**Tiếng Việt:** ![Hình ảnh 0_0](images/page_19_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 279, 883, 360]]<|/thông tin chi tiết|>
<center>Hình 13: Các cơ chế quên lãng là một trong những đặc điểm cơ bản nhất của trí nhớ con người. Phương pháp nén dữ liệu dựa trên nguyên lý này có thể mô phỏng cơ chế này bằng cách hiển thị các đoạn văn bản đã được sử dụng trước đó lên các hình ảnh để thực hiện việc nén ban đầu; sau đó, kích thước của các hình ảnh đó sẽ được điều chỉnh dần theo từng bước nhằm đạt được mức độ nén đa tầng. Trong quá trình này, số lượng các ký tự xuất hiện trong các hình ảnh sẽ giảm dần, và nội dung văn bản trên những hình ảnh đó cũng sẽ trở nên mờ nhạt hơn, qua đó thực hiện việc “quên lãng” thông tin đó.</center>

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 627, 258, 644]]<|/det|>
## 6. Conclusion  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 384, 881, 499]]<|/det|>  
Đối với các trường hợp sử dụng trong quá khứ, chúng ta có thể dần dần giảm kích thước của các hình ảnh được hiển thị để tiếp tục giảm mức tiêu thụ tài nguyên. Giả định này lấy cảm hứng từ mối tương đồng tự nhiên giữa sự suy giảm khả năng ghi nhớ của con người theo thời gian và sự suy giảm khả năng nhận diện hình ảnh theo khoảng cách không gian – cả hai đều thể hiện những quy luật tương tự về việc mất dần thông tin theo thời gian, như được minh họa trong Hình 13. Bằng cách kết hợp các cơ chế này, phương pháp nén hình ảnh dựa trên nguyên lý này cho phép tạo ra một quá trình “mất dần thông tin” tương ứng với đường cong quên lãng sinh học: thông tin mới được lưu trữ với độ chính xác cao, trong khi thông tin cũ dần bị mất đi do tỷ lệ nén tăng lên.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 657, 882, 820]]<|/det|>
In this technical report, we propose DeepSeek- OCR and preliminarily validate the feasibility of contexts optical compression through this model, demonstrating that the model can effectively decode text tokens exceeding 10 times the quantity from a small number of vision tokens. We believe this finding will facilitate the development of VLMs and LLMs in the future. Additionally, DeepSeek- OCR is a highly practical model capable of large- scale pretraining data production, serving as an indispensable assistant for LLMs. Of course, OCR alone is insufficient to fully validate true context optical compression and we will conduct digital- optical text interleaved pretraining, needle- in- a- haystack testing, and other evaluations in the future. From another perspective, optical contexts compression still offers substantial room for research and improvement, representing a promising new direction.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 505, 882, 603]]<|/det|>  
Mặc dù những nghiên cứu ban đầu cho thấy tiềm năng trong việc xử lý các dữ liệu ngữ cảnh có quy mô lớn, trong đó các thông tin ngữ cảnh mới vẫn giữ được độ phân giải cao trong khi các thông tin ngữ cảnh cũ tiêu tốn ít tài nguyên hơn, chúng tôi cũng nhận thức rằng đây vẫn là những nghiên cứu ở giai đoạn sơ bộ và cần được tiếp tục khám phá thêm. Phương pháp này mở ra hướng đi để xây dựng các kiến trúc xử lý ngữ cảnh có khả năng xử lý lượng dữ liệu lớn một cách hiệu quả, đồng thời cân bằng giữa việc lưu trữ thông tin và các hạn chế về mặt tính toán; tuy nhiên, những ứng dụng thực tế và những hạn chế của các hệ thống nén dữ liệu loại này vẫn cần được nghiên cứu sâu hơn trong các công trình khoa học tương lai.

---

**English:** 
============================================================
--- Page 20 ---
============================================================

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 627, 258, 644]]<|/det|>
## 6. Kết luận

---

**English:** <|ref|>sub_title<|/ref|><|det|>[[115, 98, 227, 116]]<|/det|>
## References  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 657, 882, 820]]<|/det|>  
Trong báo cáo kỹ thuật này, chúng tôi đề xuất mô hình DeepSeek-OCR và đã kiểm chứng sơ bộ khả năng thực hiện việc nén thông tin văn bản dựa trên ngữ cảnh thông qua mô hình này. Kết quả cho thấy mô hình có thể giải mã các đoạn văn bản dài gấp hơn 10 lần so với số lượng dữ liệu hình ảnh được sử dụng để huấn luyện, chỉ từ một lượng dữ liệu nhỏ. Chúng tôi tin rằng phát hiện này sẽ góp phần thúc đẩy sự phát triển của các mô hình VLM và LLM trong tương lai. Ngoài ra, DeepSeek-OCR còn là một mô hình rất hữu ích, có khả năng tạo ra lượng lớn dữ liệu để huấn luyện mô hình trước khi chúng được sử dụng thực tế, từ đó trở thành công cụ hỗ trợ không thể thiếu cho các mô hình LLM. Tất nhiên, việc áp dụng công nghệ OCR một mình là chưa đủ để kiểm chứng đầy đủ tính hiệu quả của phương pháp nén thông tin văn bản dựa trên ngữ cảnh; chúng tôi sẽ tiếp tục tiến hành các bài kiểm tra bổ sung trong tương lai. Từ góc độ khác, lĩnh vực nén thông tin văn bản dựa trên ngữ cảnh vẫn còn nhiều tiềm năng để nghiên cứu và cải tiến, đây chính là một hướng đi đầy hứa hẹn cho tương lai.

---

**English:** <|ref|>text<|/ref|><|det|>[[117, 125, 884, 904]]<|/det|>
[1] Marker. URL https://github.com/datalab- to/marker. [2] Mathpix. URL https://mathpix.com/. [3] Ocrflux, 2025. URL https://github.com/chatdoc- com/OCRFlux. [4] G. AI. Gemini 2.5- pro, 2025. URL https://gemini.google.com/. [5] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, H. Zhong, Y. Zhu, M. Yang, Z. Li, J. Wan, P. Wang, W. Ding, Z. Fu, Y. Xu, J. Ye, X. Zhang, T. Xie, Z. Cheng, H. Zhang, Z. Yang, H. Xu, and J. Lin. Qwen2.5- vl technical report. arXiv preprint arXiv:2502.13923, 2025. [6] L. Blecher, G. Cucurull, T. Scialom, and R. Stojnic. Nougat: Neural optical understanding for academic documents. arXiv preprint arXiv:2308.13418, 2023. [7] J. Chen, L. Kong, H. Wei, C. Liu, Z. Ge, L. Zhao, J. Sun, C. Han, and X. Zhang. Onechart: Purify the chart structural extraction via one auxiliary token. In Proceedings of the 32nd ACM International Conference on Multimedia, pages 147- 155, 2024. [8] Z. Chen, W. Wang, H. Tian, S. Ye, Z. Gao, E. Cui, W. Tong, K. Hu, J. Luo, Z. Ma, et al. How far are we to gpt- 4v? closing the gap to commercial multimodal models with open- source suites. arXiv preprint arXiv:2404.16821, 2024. [9] C. Cui, T. Sun, M. Lin, T. Gao, Y. Zhang, J. Liu, X. Wang, Z. Zhang, C. Zhou, H. Liu, et al. Paddleocr 3.0 technical report. arXiv preprint arXiv:2507.05595, 2025. [10] M. Dehghani, J. Djolonga, B. Mustafa, P. Padlewski, J. Heek, J. Gilmer, A. Steiner, M. Caron, R. Geirhos, I. Alabdulmohsin, et al. Patch n' pack: Navit, a vision transformer for any aspect ratio and resolution. Advances in Neural Information Processing Systems, 36:3632- 3656, 2023. [11] H. Feng, S. Wei, X. Fei, W. Shi, Y. Han, L. Liao, J. Lu, B. Wu, Q. Liu, C. Lin, et al. Dolphin: Document image parsing via heterogeneous anchor prompting. arXiv preprint arXiv:2505.14059, 2025. [12] Y. Goyal, T. Khot, D. Summers- Stay, D. Batra, and D. Parikh. Making the v in vqa matter: Elevating the role of image understanding in visual question answering. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 6904- 6913, 2017. [13] J. Gu, X. Meng, G. Lu, L. Hou, N. Minzhe, X. Liang, L. Yao, R. Huang, W. Zhang, X. Jiang, et al. Wukong: A 100 million large- scale chinese cross- modal pre- training benchmark. Advances in Neural Information Processing Systems, 35:26418- 26431, 2022. [14] High- flyer. HAI- LLM: Efficient and lightweight training tool for large models, 2023. URL https://www.high- flyer.cn/en/blog/hai- llm.[15] S. Iyer, X. V. Lin, R. Pasunuru, T. Mihaylov, D. Simig, P. Yu, K. Shuster, T. Wang, Q. Liu, P. S. Koura, et al. Opt- iml: Scaling language model instruction meta learning through the lens of generalization. arXiv preprint arXiv:2212.12017, 2022. [16] S. Kazemzadeh, V. Ordonez, M. Matten, and T. Berg. Referitgame: Referring to objects in photographs of natural scenes. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pages 787- 798, 2014.

**Tiếng Việt:** ============================================================
--- Trang 20 ---
============================================================

---

**English:** 
============================================================
--- Page 21 ---
============================================================

**Tiếng Việt:** <|ref|>sub_title<|/ref|><|det|>[[115, 98, 227, 116]]<|/det|>
## Tài liệu tham khảo

---

**English:** <|ref|>text<|/ref|><|det|>[[113, 100, 885, 135]]<|/det|>
[17] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.- Y. Lo, et al. Segment anything. arXiv preprint arXiv:2304.02643, 2023.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[117, 125, 884, 904]]<|/det|>
[1] Marker. Địa chỉ URL: https://github.com/datalab-to/marker. [2] Mathpix. Địa chỉ URL: https://mathpix.com/. [3] Ocrflux, 2025. Địa chỉ URL: https://github.com/chatdoc-com/OCRFlux. [4] G. AI. Gemini 2.5-pro, 2025. Địa chỉ URL: https://gemini.google.com/. [5] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, H. Zhong, Y. Zhu, M. Yang, Z. Li, J. Wan, P. Wang, W. Ding, Z. Fu, Y. Xu, J. Ye, X. Zhang, T. Xie, Z. Cheng, H. Zhang, Z. Yang, H. Xu và J. Lin. Báo cáo kỹ thuật về Qwen2.5-vl. Bản thảo trên arXiv: arXiv:2502.13923, 2025. [6] L. Blecher, G. Cucurull, T. Scialom và R. Stojnic. Nougat: Công cụ hỗ trợ việc phân tích nội dung các tài liệu học thuật thông qua công nghệ thị giác nhân tạo. Bản thảo trên arXiv: arXiv:2308.13418, 2023. [7] J. Chen, L. Kong, H. Wei, C. Liu, Z. Ge, L. Zhao, J. Sun, C. Han và X. Zhang. Onechart: Phương pháp trích xuất thông tin từ biểu đồ thông qua một ký hiệu hỗ trợ đặc biệt. Trong ấn phẩm của Hội nghị Quốc tế về Đa phương tiện truyền thông lần thứ 32 của ACM, trang 147–155, 2024. [8] Z. Chen, W. Wang, H. Tian, S. Ye, Z. Gao, E. Cui, W. Tong, K. Hu, J. Luo, Z. Ma và cộng sự. Chúng ta còn cách bằng mấy so với mô hình GPT-4v? Cách nào để thu hẹp khoảng cách với các mô hình đa phương tiện thương mại sử dụng các bộ công cụ mã nguồn mở? Bản thảo trên arXiv: arXiv:2404.16821, 2024. [9] C. Cui, T. Sun, M. Lin, T. Gao, Y. Zhang, J. Liu, X. Wang, Z. Zhang, C. Zhou, H. Liu và cộng sự. Báo cáo kỹ thuật về Paddleocr 3.0. Bản thảo trên arXiv: arXiv:2507.05595, 2025. [10] M. Dehghani, J. Djolonga, B. Mustafa, P. Padlewski, J. Heek, J. Gilmer, A. Steiner, M. Caron, R. Geirhos, I. Alabdulmohsin và cộng sự. Patch n’ Pack: Navit – một công cụ xử lý hình ảnh linh hoạt, phù hợp với mọi tỷ lệ khung hình và độ phân giải. Tạp chí Advances in Neural Information Processing Systems, tập 36, trang 3632–3656, 2023. [11] H. Feng, S. Wei, X. Fei, W. Shi, Y. Han, L. Liao, J. Lu, B. Wu, Q. Liu, C. Lin và cộng sự. Dolphin: Phương pháp phân tích hình ảnh tài liệu thông qua các gợi ý đa dạng. Bản thảo trên arXiv: arXiv:2505.14059, 2025. [12] Y. Goyal, T. Khot, D. Summers-Stay, D. Batra và D. Parikh. Tăng tầm quan trọng của khả năng hiểu hình ảnh trong việc trả lời câu hỏi hình ảnh. Trong Tài liệu hội nghị IEEE về thị giác máy tính và nhận diện mẫu, trang 6904–6913, 2017. [13] J. Gu, X. Meng, G. Lu, L. Hou, N. Minzhe, X. Liang, L. Yao, R. Huang, W. Zhang, X. Jiang và cộng sự. Wukong: Mô hình huấn luyện đa模态 quy mô lớn, sử dụng dữ liệu tiếng Trung, được phát triển bởi 100 triệu dữ liệu. Tạp chí Advances in Neural Information Processing Systems, 35:26418–26431, 2022. [14] High- flyer. HAI-LLM: Công cụ huấn luyện hiệu quả và nhẹ nhàng cho các mô hình lớn, 2023. Địa chỉ web: https://www.high- flyers.cn/en/blog/hai-llm. [15] S. Iyer, X. V. Lin, R. Pasunuru, T. Mihaylov, D. Simig, P. Yu, K. Shuster, T. Wang, Q. Liu, P. S. Koura và cộng sự. Opt-Iml: Phương pháp học máy để tối ưu hóa quá trình huấn luyện các mô hình ngôn ngữ, dựa trên khả năng tổng quát hóa. Bản thảo trên arXiv: arXiv:2212.12017, 2022. [16] S. Kazemzadeh, V. Ordonez, M. Matten và T. Berg. Referitgame: Công cụ nhận diện đối tượng trong các hình ảnh về cảnh thiên nhiên. Trong Tài liệu hội nghị EMNLP năm 2014 về các phương pháp thực nghiệm trong xử lý ngôn ngữ tự nhiên, trang 787–798, 2014.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 143, 884, 192]]<|/det|>
[18] Z. Li, Y. Liu, Q. Liu, Z. Ma, Z. Zhang, S. Zhang, Z. Guo, J. Zhang, X. Wang, and X. Bai. Monkeyocr: Document parsing with a structure-recognition- relation triplet paradigm. arXiv preprint arXiv:2506.05218, 2025.  

**Tiếng Việt:** ============================================================
--- Trang 21 ---
============================================================

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 201, 884, 251]]<|/det|>
[19] A. Liu, B. Feng, B. Wang, B. Wang, B. Liu, C. Zhao, C. Dengr, C. Ruan, D. Dai, D. Guo, et al. Deepseek- v2: A strong, economical, and efficient mixture- of- experts language model. arXiv preprint arXiv:2405.04434, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[113, 100, 885, 135]]<|/det|>  
[17] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.-Y. Lo và cộng sự. “Việc phân đoạn bất cứ thứ gì đều trở nên khả thi.” Bản thảo trên arXiv: arXiv:2304.02643, 2023.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 260, 884, 294]]<|/det|>
[20] A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, et al. Deepseek- v3 technical report. arXiv preprint arXiv:2412.19437, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 143, 884, 192]]<|/det|>  
[18] Z. Li, Y. Liu, Q. Liu, Z. Ma, Z. Zhang, S. Zhang, Z. Guo, J. Zhang, X. Wang và X. Bai. Monkeyocr: Phương pháp phân tích văn bản dựa trên mô hình ba yếu tố – cấu trúc, mối quan hệ giữa các thành phần trong văn bản. Bản thảo nghiên cứu trên arXiv: arXiv:2506.05218, 2025.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 303, 884, 353]]<|/det|>
[21] C. Liu, H. Wei, J. Chen, L. Kong, Z. Ge, Z. Zhu, L. Zhao, J. Sun, C. Han, and X. Zhang. Focus anywhere for fine- grained multi- page document understanding. arXiv preprint arXiv:2405.14295, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 201, 884, 251]]<|/det|>  
[19] A. Liu, B. Feng, B. Wang, B. Wang, B. Liu, C. Zhao, C. Deng, C. Ruan, D. Dai, D. Guo và cộng sự. Deepseek-v2: Một mô hình ngôn ngữ dựa trên kết hợp ý kiến của nhiều chuyên gia, vừa mạnh mẽ, vừa tiết kiệm tài nguyên và hiệu quả trong việc xử lý dữ liệu. Bản thảo gốc trên arXiv: arXiv:2405.04434, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 362, 881, 395]]<|/det|>
[22] I. Loshchilov and F. Hutter. Sgdr: Stochastic gradient descent with warm restarts. arXiv preprint arXiv:1608.03983, 2016.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 260, 884, 294]]<|/det|>  
[20] A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan và cộng sự. Báo cáo kỹ thuật về Deepseek-v3. Bản thảo trên arXiv: arXiv:2412.19437, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 404, 830, 422]]<|/det|>
[23] I. Loshchilov and F. Hutter. Decoupled weight decay regularization. In ICLR, 2019.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 303, 884, 353]]<|/det|>  
[21] C. Liu, H. Wei, J. Chen, L. Kong, Z. Ge, Z. Zhu, L. Zhao, J. Sun, C. Han và X. Zhang. Khả năng hiểu nội dung các tài liệu gồm nhiều trang một cách chi tiết, bất kể vị trí nào được chọn làm điểm tập trung. Bản thảo trên arXiv: arXiv:2405.14295, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 431, 884, 481]]<|/det|>
[24] A. Masry, D. X. Long, J. Q. Tan, S. Joty, and E. Hoque. Chartqa: A benchmark for question answering about charts with visual and logical reasoning. arXiv preprint arXiv:2203.10244, 2022.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 362, 881, 395]]<|/det|>
[22] I. Loshchilov và F. Hutter. Phương pháp hạ dốc gradient ngẫu nhiên với cơ chế khởi động lại. Bản thảo trên arXiv: arXiv:1608.03983, 2016.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 490, 884, 555]]<|/det|>
[25] A. Nassar, A. Marafioti, M. Omenetti, M. Lysak, N. Livathinos, C. Auer, L. Morin, R. T. de Lima, Y. Kim, A. S. Gurbuz, et al. Smoldocling: An ultra- compact vision- language model for end- to- end multi- modal document conversion. arXiv preprint arXiv:2503.11576, 2025.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 404, 830, 422]]<|/det|>
[23] I. Loshchilov và F. Hutter. Phương pháp điều chỉnh độ suy giảm trọng số không phụ thuộc lẫn nhau. Trong hội nghị ICLR, 2019.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 565, 461, 583]]<|/det|>
[26] OpenAI. Gpt- 4 technical report, 2023.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 431, 884, 481]]<|/det|>  
[24] A. Masry, D. X. Long, J. Q. Tan, S. Joty và E. Hoque. Chartqa: Một công cụ đánh giá hiệu suất các hệ thống trả lời câu hỏi liên quan đến biểu đồ, với khả năng suy luận vừa dựa trên thông tin trực quan vừa dựa trên lô-gic. Bản thảo nghiên cứu trên arXiv: arXiv:2203.10244, 2022.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 592, 884, 658]]<|/det|>
[27] L. Ouyang, Y. Qu, H. Zhou, J. Zhu, R. Zhang, Q. Lin, B. Wang, Z. Zhao, M. Jiang, X. Zhao, et al. Omnidocbench: Benchmarking diverse pdf document parsing with comprehensive annotations. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 24838- 24848, 2025.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 490, 884, 555]]<|/det|>  
[25] A. Nassar, A. Marafioti, M. Omenetti, M. Lysak, N. Livathinos, C. Auer, L. Morin, R. T. de Lima, Y. Kim, A. S. Gurbuz và cộng sự. Smoldocling: Một mô hình học máy siêu nhỏ gọn dành cho việc chuyển đổi tài liệu đa phương thức một cách tự động. Bản thảo trên arXiv: arXiv:2503.11576, 2025.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 667, 884, 716]]<|/det|>
[28] J. Poznanski, A. Rangapur, J. Borchardt, J. Dunkelberger, R. Huff, D. Lin, C. Wilhelm, K. Lo, and L. Soldaini. olmocr: Unlocking trillions of tokens in pdfs with vision language models. arXiv preprint arXiv:2502.18443, 2025.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 565, 461, 583]]<|/det|>
[26] OpenAI. Báo cáo kỹ thuật về GPT-4, 2023.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 726, 884, 791]]<|/det|>
[29] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language supervision. In International conference on machine learning, pages 8748- 8763. PMLR, 2021.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 592, 884, 658]]<|/det|>
[27] L. Ouyang, Y. Qu, H. Zhou, J. Zhu, R. Zhang, Q. Lin, B. Wang, Z. Zhao, M. Jiang, X. Zhao và cộng sự. Omnidocbench: Công cụ đánh giá hiệu suất các phương pháp xử lý tài liệu PDF với các bình luận chi tiết. Trong Tài liệu hội nghị Thị giác máy tính và Nhận dạng mẫu, trang 24838–24848, năm 2025.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 801, 839, 819]]<|/det|>
[30] Rednote. dots.ocr, 2025. URL https://github.com/rednote- hilab/dots.ocr.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 667, 884, 716]]<|/det|>  
[28] J. Poznanski, A. Rangapur, J. Borchardt, J. Dunkelberger, R. Huff, D. Lin, C. Wilhelm, K. Lo và L. Soldaini. olmocr: Giải mã hàng nghìn tỷ token trong các tệp PDF bằng các mô hình ngôn ngữ hình ảnh. Bản thảo trên arXiv: arXiv:2502.18443, 2025.

---

**English:** <|ref|>text<|/ref|><|det|>[[115, 828, 884, 877]]<|/det|>
[31] C. Schuhmann, R. Vencu, R. Beaumont, R. Kaczmarczyk, C. Mullis, A. Katta, T. Coombes, J. Jitsev, and A. Komatsuzaki. Laion- 400m: Open dataset of clip- filtered 400 million image- text pairs. arXiv preprint arXiv:2111.02114, 2021.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 726, 884, 791]]<|/det|>  
[29] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark và cộng sự. Việc xây dựng các mô hình thị giác có khả năng được áp dụng rộng rãi thông qua việc học từ dữ liệu ngôn ngữ tự nhiên. Trong Hội nghị Quốc tế về Máy học, trang 8748–8763. PMLR, 2021.

---

**English:** 
============================================================
--- Page 22 ---
============================================================

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 801, 839, 819]]<|/det|>  
[30] Rednote. dots.ocr, 2025. Địa chỉ URL: https://github.com/rednote-hilab/dots.ocr.

---

**English:** <|ref|>text<|/ref|><|det|>[[113, 99, 885, 151]]<|/det|>
[32] A. Singh, V. Natarajan, M. Shah, Y. Jiang, X. Chen, D. Batra, D. Parikh, and M. Rohrbach. Towards vqa models that can read. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 8317- 8326, 2019.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[115, 828, 884, 877]]<|/det|>  
[31] C. Schuhmann, R. Vencu, R. Beaumont, R. Kaczmarczyk, C. Mullis, A. Katta, T. Coombes, J. Jitsev và A. Komatsuzaki. Laion-400m: Bộ dữ liệu mở chứa 400 triệu cặp hình ảnh kèm văn bản đã được lọc. Bản thảo trên arXiv: arXiv:2111.02114, 2021.

---

**English:** <|ref|>text<|/ref|><|det|>[[113, 157, 884, 192]]<|/det|>
[33] T. Sun, C. Cui, Y. Du, and Y. Liu. Pp- dcolayout: A unified document layout detection model to accelerate large- scale data construction. arXiv preprint arXiv:2503.17213, 2025.  

**Tiếng Việt:** ============================================================
--- Trang 22 ---
============================================================

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 201, 884, 251]]<|/det|>
[34] B. Wang, C. Xu, X. Zhao, L. Ouyang, F. Wu, Z. Zhao, R. Xu, K. Liu, Y. Qu, F. Shang, et al. Mineru: An open- source solution for precise document content extraction. arXiv preprint arXiv:2409.18839, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[113, 99, 885, 151]]<|/det|>  
[32] A. Singh, V. Natarajan, M. Shah, Y. Jiang, X. Chen, D. Batra, D. Parikh và M. Rohrbach. Những nỗ lực nhằm phát triển các mô hình nhận diện hình ảnh có khả năng “đọc” thông tin. Trong tài liệu báo cáo hội nghị IEEE/CVF về thị giác máy tính và nhận dạng mẫu, trang 8317–8326, năm 2019.

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 260, 884, 310]]<|/det|>
[35] P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge, et al. Qwen2- vl: Enhancing vision- language model's perception of the world at any resolution. arXiv preprint arXiv:2409.12191, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[113, 157, 884, 192]]<|/det|>  
[33] T. Sun, C. Cui, Y. Du và Y. Liu. Pp-dcolayout: Một mô hình thống nhất để phát hiện cách bố trí nội dung tài liệu, nhằm tăng tốc độ xử lý dữ liệu quy mô lớn. Bản thảo trên arXiv: arXiv:2503.17213, 2025.

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 319, 884, 370]]<|/det|>
[36] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, J. Yang, J. Sun, C. Han, and X. Zhang. Vary: Scaling up the vision vocabulary for large vision- language model. In European Conference on Computer Vision, pages 408- 424. Springer, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[114, 201, 884, 251]]<|/det|>  
[34] B. Wang, C. Xu, X. Zhao, L. Ouyang, F. Wu, Z. Zhao, R. Xu, K. Liu, Y. Qu, F. Shang, v.v. Mineru: Một giải pháp mã nguồn mở dùng để trích xuất nội dung tài liệu một cách chính xác. Bản thảo trên arXiv: arXiv:2409.18839, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 378, 884, 428]]<|/det|>
[37] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, E. Yu, J. Sun, C. Han, and X. Zhang. Small language model meets with reinforced vision vocabulary. arXiv preprint arXiv:2401.12503, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[114, 260, 884, 310]]<|/det|>
[35] P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge và cộng sự. Qwen2-vl: Nâng cao khả năng nhận thức thế giới của các mô hình học máy ngôn ngữ-viễn thị ở mọi độ phân giải. Bản thảo trên arXiv: arXiv:2409.12191, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 436, 884, 487]]<|/det|>
[38] H. Wei, C. Liu, J. Chen, J. Wang, L. Kong, Y. Xu, Z. Ge, L. Zhao, J. Sun, Y. Peng, et al. General ocr theory: Towards ocr- 2.0 via a unified end- to- end model. arXiv preprint arXiv:2409.01704, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[114, 319, 884, 370]]<|/det|>
[36] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, J. Yang, J. Sun, C. Han và X. Zhang. Vary: Phương pháp mở rộng vốn từ ngữ liên quan đến hình ảnh dành cho các mô hình ngôn ngữ-viễn thị quy mô lớn. Trong Hội nghị Châu Âu về Thị giác Máy tính, trang 408–424. Springer, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[113, 495, 884, 530]]<|/det|>
[39] H. Wei, Y. Yin, Y. Li, J. Wang, L. Zhao, J. Sun, Z. Ge, X. Zhang, and D. Jiang. Slow perception: Let's perceive geometric figures step- by- step. arXiv preprint arXiv:2412.20631, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[114, 378, 884, 428]]<|/det|>  
[37] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, E. Yu, J. Sun, C. Han và X. Zhang. Mô hình ngôn ngữ nhỏ kết hợp với bộ từ vựng hỗ trợ thị giác. Bản thảo trên arXiv: arXiv:2401.12503, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 538, 884, 589]]<|/det|>
[40] Z. Wu, X. Chen, Z. Pan, X. Liu, W. Liu, D. Dai, H. Gao, Y. Ma, C. Wu, B. Wang, et al. Deepseek- vl2: Mixture- of- experts vision- language models for advanced multimodal understanding. arXiv preprint arXiv:2412.10302, 2024.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[114, 436, 884, 487]]<|/det|>  
[38] H. Wei, C. Liu, J. Chen, J. Wang, L. Kong, Y. Xu, Z. Ge, L. Zhao, J. Sun, Y. Peng và cộng sự. Lý thuyết chung về công nghệ nhận dạng ký tự quang học: Hướng tới phiên bản OCR 2.0 thông qua một mô hình tích hợp từ đầu đến cuối. Bản thảo trên arXiv: arXiv:2409.01704, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[113, 597, 884, 632]]<|/det|>
[41] W. Yu, Z. Yang, L. Li, J. Wang, K. Lin, Z. Liu, X. Wang, and L. Wang. Mm- vet: Evaluating large multimodal models for integrated capabilities. arXiv preprint arXiv:2308.02490, 2023.  

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[113, 495, 884, 530]]<|/det|>  
[39] H. Wei, Y. Yin, Y. Li, J. Wang, L. Zhao, J. Sun, Z. Ge, X. Zhang và D. Jiang. Nhận thức chậm rãi: Hãy cùng nhận diện các hình học một cách từng bước một. Bản thảo trên arXiv: arXiv:2412.20631, 2024.

---

**English:** <|ref|>text<|/ref|><|det|>[[114, 640, 884, 690]]<|/det|>
[42] J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao, et al. Internvl3: Exploring advanced training and test- time recipes for open- source multimodal models. arXiv preprint arXiv:2504.10479, 2025.

**Tiếng Việt:** <|ref|>text<|/ref|><|det|>[[114, 538, 884, 589]]<|/det|>
[40] Z. Wu, X. Chen, Z. Pan, X. Liu, W. Liu, D. Dai, H. Gao, Y. Ma, C. Wu, B. Wang và cộng sự. Deepseek-vl2: Các mô hình học máy thị giác-ngôn ngữ dựa trên kết hợp kiến thức của nhiều chuyên gia, nhằm nâng cao khả năng hiểu biết đa phương thức. Bản thảo trước khi công bố trên arXiv: arXiv:2412.10302, 2024.

---

