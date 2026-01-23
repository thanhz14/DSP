

============================================================
--- Trang 1 ---  
============================================================

<|ref|>title<|/ref|><|det|>[[205, 132, 790, 157]]<|/det|>
# DeepSeek-OCR: Kỹ thuật nén dữ liệu quang học dựa trên ngữ cảnh

<|ref|>text<|/ref|><|det|>[[350, 187, 646, 203]]<|/det|>  
Haoran Wei, Yaofeng Sun, Yukun Li

<|ref|>text<|/ref|><|det|>[[444, 215, 551, 230]]<|/det|>
DeepSeek – Trí tuệ nhân tạo

<|ref|>sub_title<|/ref|><|det|>[[450, 263, 547, 283]]<|/det|>
## Tóm tắt

<|ref|>text<|/ref|><|det|>[[115, 306, 883, 564]]<|/det|>
We present DeepSeek- OCR as an initial investigation into the feasibility of compressing long contexts via optical 2D mapping. DeepSeek- OCR consists of two components: DeepEncoder and DeepSeek3B- MoE- A570M as the decoder. Specifically, DeepEncoder serves as the core engine, designed to maintain low activations under high- resolution input while achieving high compression ratios to ensure an optimal and manageable number of vision tokens. Experiments show that when the number of text tokens is within 10 times that of vision tokens (i.e., a compression ratio \(< 10\times\) ), the model can achieve decoding (OCR) precision of \(97\%\). Even at a compression ratio of \(20\times\), the OCR accuracy still remains at about \(60\%\). This shows considerable promise for research areas such as historical long- context compression and memory forgetting mechanisms in LLMs. Beyond this, DeepSeek- OCR also demonstrates high practical value. On OmniDocBench, it surpasses GOT- OCR2.0 (256 tokens/page) using only 100 vision tokens, and outperforms MinerU2.0 (6000+ tokens per page on average) while utilizing fewer than 800 vision tokens. In production, DeepSeek- OCR can generate training data for LLMs/VLMs at a scale of \(200k+\) pages per day (a single A100- 40G). Codes and model weights are publicly accessible at http://github.com/deepseek- ai/DeepSeek- OCR.<|ref|>text<|/ref|><|det|>[[115, 306, 883, 564]]<|/det|>  
Chúng tôi giới thiệu DeepSeek-OCR như một nghiên cứu sơ bộ về khả năng nén các đoạn văn dài thông qua phương pháp lập bản đồ 2D quang học. DeepSeek-OCR bao gồm hai thành phần chính: DeepEncoder và DeepSeek3B-MoE-A570M, trong đó DeepEncoder đóng vai trò là bộ phận xử lý chính; nó được thiết kế để duy trì mức độ hoạt động thấp ngay cả với các dữ liệu đầu vào có độ phân giải cao, đồng thời đạt được tỷ lệ nén cao nhằm đảm bảo số lượng các “token” hình ảnh được sử dụng là vừa phải và dễ quản lý. Các thí nghiệm cho thấy khi số lượng token văn bản chỉ bằng khoảng 1/10 so với số lượng token hình ảnh (tức tỷ lệ nén < 10 lần), mô hình vẫn có thể đạt độ chính xác trong việc giải mã văn bản lên đến 97%. Ngay cả ở tỷ lệ nén 20 lần, độ chính xác vẫn khoảng 60%. Điều này mở ra nhiều tiềm năng cho các lĩnh vực nghiên cứu như việc nén các đoạn văn dài có tính lịch sử hoặc cơ chế “quên lãng” thông tin trong các mô hình LLM. Ngoài ra, DeepSeek-OCR còn thể hiện giá trị thực tiễn cao: trên nền tảng OmniDocBench, nó vượt trội hơn so với GOT-OCR2.0 (sử dụng 256 token/trang) khi chỉ cần 100 token hình ảnh; đồng thời cũng vượt trội hơn MinerU2.0 (trung bình sử dụng hơn 6000 token/trang) mà vẫn chỉ tiêu thụ chưa đầy 800 token hình ảnh. Trong thực tế ứng dụng, DeepSeek-OCR có thể tạo ra lượng dữ liệu huấn luyện lớn cho các mô hình LLM/VLM, với tốc độ lên đến hơn 200.000 trang mỗi ngày (sử dụng một card GPU loại A100-40G). Mã nguồn và thông tin về cấu hình mô hình có thể được tìm thấy tại địa chỉ http://github.com/deepseek-ai/DeepSeek-OCR.

![Hình 0_0](images/page_1_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 827, 881, 892]]<|/thông tin chi tiết|>
<center>Hình 1: Hình (a) thể hiện tỷ lệ nén (số lượng các ký hiệu văn bản so với số lượng các ký hiệu hình ảnh được mô hình sử dụng) khi thử nghiệm trên bài kiểm thử Fox [21]; Hình (b) so sánh hiệu suất của mô hình DeepSeek-OCR trên nền tảng OmniDocBench [27]. DeepSeek-OCR đạt được mức hiệu suất hàng đầu trong số các mô hình end-to-end, trong khi chỉ sử dụng số lượng ký hiệu hình ảnh tối thiểu.</center>

============================================================
--- Trang 2 ---  
============================================================

<|ref|>sub_title<|/ref|><|det|>[[115, 99, 210, 117]]<|/det|>
## Nội dung

<|ref|>text<|/ref|><|det|>[[115, 140, 884, 158]]<|/det|>  
1. Giới thiệu 3

<|ref|>văn bản<|/ref|><|det|>[[115, 175, 884, 193]]<|/det|>
2 Các tác phẩm liên quan 4

<|ref|>text<|/ref|><|det|>[[140, 199, 884, 216]]<|/det|>
2.1 Các bộ mã hóa hình ảnh điển hình trong các mô hình nhận diện hình ảnh ảo 4

<|ref|>text<|/ref|><|det|>[[140, 222, 884, 239]]<|/det|>
2.2 Các mô hình OCR hoạt động theo nguyên lý từ đầu đến cuối 4

<|ref|>text<|/ref|><|det|>[[115, 257, 884, 275]]<|/det|>  
3 Phương pháp luận 5

<|ref|>text<|/ref|><|det|>[[140, 280, 884, 297]]<|/det|>
3.1 Kiến trúc 5

<|ref|>text<|/ref|><|det|>[[140, 303, 884, 320]]<|/det|>
3.2 DeepEncoder 5

<|ref|>text<|/ref|><|det|>[[180, 326, 884, 343]]<|/det|>
3.2.1 Cấu trúc của DeepEncoder 5

<|ref|>text<|/ref|><|det|>[[180, 349, 884, 366]]<|/det|>
3.2.2 Hỗ trợ nhiều độ phân giải khác nhau 6

<|ref|>text<|/ref|><|det|>[[140, 371, 884, 389]]<|/det|>
3.3 Bộ giải mã MoE 7

<|ref|>text<|/ref|><|det|>[[140, 394, 884, 411]]<|/det|>
3.4 Máy chạy dữ liệu 7

<|ref|>text<|/ref|><|det|>[[180, 417, 884, 433]]<|/det|>
3.4.1 Dữ liệu OCR 1.0 7

<|ref|>text<|/ref|><|det|>[[180, 440, 884, 456]]<|/det|>  
Dữ liệu OCR 2.0 phiên bản 8

<|ref|>text<|/ref|><|det|>[[180, 462, 884, 479]]<|/det|>
3.4.3 Dữ liệu thị giác tổng quát 9

<|ref|>văn bản<|/ref|><|det|>[[180, 485, 884, 501]]<|/det|>
3.4.4 Dữ liệu chỉ chứa văn bản 9

<|ref|>text<|/ref|><|det|>[[140, 506, 884, 524]]<|/det|>
3.5 Quy trình đào tạo 9

<|ref|>text<|/ref|><|det|>[[180, 529, 884, 546]]<|/det|>
3.5.1 Đào tạo mô hình DeepEncoder 10

<|ref|>text<|/ref|><|det|>[[180, 551, 884, 568]]<|/det|>
3.5.2 Đào tạo mô hình DeepSeek-OCR 10

<|ref|>text<|/ref|><|det|>[[115, 586, 884, 603]]<|/det|>
4 Đánh giá 10

<|ref|>text<|/ref|><|det|>[[140, 609, 884, 626]]<|/det|>
4.1 Nghiên cứu về việc nén dữ liệu văn bản dựa trên công nghệ thị giác 10

<|ref|>text<|/ref|><|det|>[[140, 632, 884, 649]]<|/det|>
4.2 Hiệu suất thực tế của công nghệ OCR 12

<|ref|>text<|/ref|><|det|>[[140, 655, 884, 672]]<|/det|>
4.3 Nghiên cứu định tính 12

<|ref|>text<|/ref|><|det|>[[180, 678, 884, 694]]<|/det|>
4.3.1 Phân tích sâu 12

<|ref|>text<|/ref|><|det|>[[180, 700, 884, 717]]<|/det|>
4.3.2 Nhận dạng ngôn ngữ đa dạng 16

<|ref|>text<|/ref|><|det|>[[180, 722, 884, 739]]<|/det|>
4.3.3 Khả năng hiểu biết tổng quát về hình ảnh 17

<|ref|>text<|/ref|><|det|>[[115, 757, 884, 774]]<|/det|>  
5. Thảo luận 18

<|ref|>văn bản<|/ref|><|det|>[[115, 792, 884, 810]]<|/det|>  
6. Kết luận 19

============================================================
--- Trang 3 ---  
============================================================

<|ref|>sub_title<|/ref|><|det|>[[117, 99, 270, 116]]<|/det|>
## 1. Giới thiệu

<|ref|>text<|/ref|><|det|>[[115, 130, 882, 227]]<|/det|>  
Các mô hình ngôn ngữ lớn hiện nay đối mặt với những thách thức lớn về mặt tính toán khi xử lý các nội dung văn bản dài, do mức độ tốn tài nguyên tăng theo cấp số nhân theo độ dài chuỗi văn bản. Chúng tôi đề xuất một giải pháp tiềm năng: tận dụng hình thức biểu đạt thông tin qua hình ảnh như một phương tiện nén hiệu quả cho dữ liệu văn bản. Một hình ảnh duy nhất chứa nội dung văn bản có thể truyền tải được nhiều thông tin hơn đáng kể so với việc sử dụng văn bản kỹ thuật số tương đương; điều này cho thấy rằng phương pháp nén thông tin thông qua hình ảnh có thể mang lại tỷ lệ nén cao hơn nhiều.

<|ref|>text<|/ref|><|det|>[[115, 235, 882, 331]]<|/det|>  
Nhận thức này thúc đẩy chúng ta xem xét lại các mô hình học máy thị giác-ngôn ngữ (Vision-Language Models – VLMs) từ góc độ tập trung vào các mô hình LLM, với trọng tâm là tìm hiểu cách các công cụ mã hóa thông tin thị giác có thể nâng cao hiệu quả xử lý dữ liệu văn bản của các mô hình LLM, thay vì chỉ tập trung vào những khả năng mà con người giỏi nhất, chẳng hạn như việc trả lời các câu hỏi đối thoại [12, 16, 24, 32, 41]. Các nhiệm vụ OCR, với vai trò là phương tiện kết nối giữa thị giác và ngôn ngữ, tạo điều kiện lý tưởng để kiểm thử mô hình này; chúng thiết lập mối quan hệ giữa quá trình nén và giải nén dữ liệu thị giác với dữ liệu văn bản một cách tự nhiên, đồng thời cung cấp các chỉ số đánh giá định lượng cần thiết.

<|ref|>text<|/ref|><|det|>[[115, 339, 880, 372]]<|/det|>  
Theo đó, chúng tôi giới thiệu DeepSeek-OCR – một hệ thống VLM được thiết kế như một bằng chứng sơ bộ về khả năng nén dữ liệu hình ảnh kết hợp văn bản một cách hiệu quả. Công trình của chúng tôi đóng góp ba điểm chính:

<|ref|>text<|/ref|><|det|>[[115, 379, 882, 509]]<|/det|>  
Trước hết, chúng tôi tiến hành phân tích định lượng toàn diện về tỷ lệ nén các đối tượng hình ảnh và văn bản. Phương pháp của chúng tôi đạt độ chính xác khi giải mã dữ liệu nén lên đến \(96\%\) ở mức độ nén \(9 – 10\times\); độ chính xác này giảm xuống khoảng \(90\%\) ở mức độ nén \(10 – 12\times\), và chỉ còn khoảng \(60\%\) ở mức độ nén \(20\times\), được thể hiện trên bài kiểm thử Fox [21] với nhiều loại cấu trúc văn bản khác nhau. Độ chính xác thực tế còn cao hơn nữa nếu xét đến sự khác biệt về định dạng giữa dữ liệu đầu ra và dữ liệu chuẩn, như được minh họa trong Hình 1(a). Kết quả này cho thấy các mô hình ngôn ngữ có kích thước nhỏ vẫn có thể học cách giải mã các dữ liệu hình ảnh đã được nén một cách hiệu quả; điều này gợi ý rằng các mô hình ngôn ngữ lớn hơn cũng hoàn toàn có thể đạt được khả năng tương tự nếu được thiết kế quá trình huấn luyện phù hợp.

Thứ hai, chúng tôi giới thiệu DeepEncoder – một kiến trúc mới mẻ giúp giảm thiểu lượng bộ nhớ cần sử dụng và số lượng các thông tin đầu vào liên quan đến hình ảnh, ngay cả với những dữ liệu có độ phân giải cao. Cấu trúc này kết nối các thành phần xử lý thông tin hình ảnh theo thứ tự: thành phần xử lý thông tin theo từng khu vực nhỏ và thành phần xử lý thông tin toàn diện, thông qua một bộ thu nhỏ dữ liệu có kích thước \(16\times\). Thiết kế này đảm bảo rằng thành phần xử lý thông tin theo từng khu vực nhỏ có thể xử lý một lượng lớn dữ liệu hình ảnh, trong khi bộ thu nhỏ này giúp giảm bớt số lượng thông tin đó trước khi chúng được chuyển đến thành phần xử lý toàn diện, từ đó nâng cao hiệu quả sử dụng bộ nhớ và giảm thiểu lượng dữ liệu cần xử lý.

<|ref|>text<|/ref|><|det|>[[115, 619, 882, 718]]<|/det|>  
Thứ ba, chúng tôi đã phát triển công cụ DeepSeek-OCR dựa trên các mô hình DeepEncoder và DeepSeek3B-MoE [19, 20]. Như được minh họa trong Hình 1(b), công cụ này đạt được hiệu suất hàng đầu trong số các mô hình end-to-end trên bộ dữ liệu OmniDocBench, trong khi chỉ sử dụng một lượng nhỏ các yếu tố liên quan đến xử lý hình ảnh. Ngoài ra, chúng tôi còn trang bị cho mô hình này khả năng phân tích các biểu đồ, công thức hóa học, hình dạng hình học đơn giản và hình ảnh tự nhiên, nhằm nâng cao tính ứng dụng thực tiễn của nó. Trong thực tế, với 20 node mỗi node được trang bị 8 GPU loại A100-40G, DeepSeek-OCR có thể tạo ra 33 triệu trang dữ liệu mỗi ngày để phục vụ các mô hình LLM hoặc VLM.

<|ref|>text<|/ref|><|det|>[[115, 725, 882, 886]]<|/det|>  
Tóm lại, nghiên cứu này đề xuất một phương pháp tiếp cận sơ bộ trong việc sử dụng các công nghệ xử lý hình ảnh như một phương tiện nén hiệu quả để xử lý thông tin văn bản trong các mô hình ngôn ngữ lớn. Thông qua công cụ DeepSeek-OCR, chúng tôi đã chứng minh rằng việc kết hợp công nghệ xử lý hình ảnh và văn bản có thể giúp giảm số lượng các ký hiệu được sử dụng trong quá trình xử lý đáng kể (từ 7 đến 20 lần), từ đó mở ra hướng đi mới để giải quyết những thách thức liên quan đến việc xử lý thông tin có ngữ cảnh dài trong các mô hình ngôn ngữ lớn. Phân tích định lượng của chúng tôi cung cấp những hướng dẫn thực tiễn cho việc tối ưu hóa cách phân bổ các ký hiệu trong các mô hình này, trong khi kiến trúc DeepEncoder được đề xuất đã chứng tỏ tính khả thi thực tế của phương pháp này thông qua các ứng dụng thực tế. Mặc dù nghiên cứu này tập trung vào công nghệ OCR như một ví dụ minh họa ý tưởng, nhưng nó mở ra nhiều khả năng mới để xem xét cách kết hợp hiệu quả giữa các công nghệ xử lý hình ảnh và ngôn ngữ, nhằm nâng cao hiệu suất tính toán trong các quá trình xử lý văn bản quy mô lớn cũng như các hệ thống tự động hóa.

============================================================
--- Trang 4 ---
============================================================

![Hình 0_0](images/page_4_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 234, 880, 268]]<|/thông tin chi tiết|>
<center>Hình 2 | Các bộ mã hóa hình ảnh phổ biến trong các hệ thống quản lý dữ liệu hình ảnh mở nguồn hiện nay. Dưới đây là ba loại bộ mã hóa thường được sử dụng; tất cả chúng đều có những hạn chế riêng.</center>

<|ref|>sub_title<|/ref|><|det|>[[117, 290, 291, 308]]<|/det|>
## 2. Các công trình liên quan

<|ref|>sub_title<|/ref|><|det|>[[117, 323, 436, 340]]<|/det|>
### 2.1. Các bộ mã hóa hình ảnh điển hình trong các mô hình nhận diện hình ảnh ảo</td>

<|ref|>text<|/ref|><|det|>[[115, 350, 882, 624]]<|/det|>  
Các công cụ xử lý hình ảnh mã nguồn mở hiện nay sử dụng ba loại bộ mã hóa hình ảnh chính, như được minh họa trong Hình 2. Loại thứ nhất là kiến trúc gồm hai “tháp” xử lý, điển hình là công cụ Vary [36]; phương pháp này sử dụng các bộ mã hóa SAM [17] để tăng số lượng tham số cần thiết cho việc xử lý hình ảnh độ phân giải cao. Mặc dù cho phép điều chỉnh các tham số và sử dụng bộ nhớ kích hoạt, phương pháp này lại gặp phải nhiều hạn chế: quá trình xử lý hình ảnh trước cần phức tạp hơn, làm tăng độ khó trong việc triển khai và khó tận dụng tính song song của các luồng xử lý trong quá trình huấn luyện. Loại thứ hai là phương pháp dựa trên việc chia hình ảnh thành các ô nhỏ để xử lý song song, điển hình là công cụ InternVL2.0 [8]; phương pháp này giúp giảm lượng bộ nhớ cần thiết khi xử lý hình ảnh độ phân giải cao. Tuy có khả năng xử lý các hình ảnh độ phân giải rất cao, nhưng phương pháp này vẫn bị hạn chế do độ phân giải của các bộ mã hóa thường khá thấp (dưới 512 × 512), khiến việc xử lý các hình ảnh lớn trở nên phức tạp hơn. Loại thứ ba là phương pháp mã hóa với độ phân giải tự động điều chỉnh, điển hình là công cụ Qwen2-VL [35]; phương pháp này áp dụng công nghệ NaViT [10] để xử lý trực tiếp toàn bộ hình ảnh mà không cần chia chúng thành các ô nhỏ. Mặc dù có khả năng thích ứng với nhiều độ phân giải khác nhau, phương pháp này vẫn gặp nhiều khó khăn khi xử lý các hình ảnh lớn do lượng bộ nhớ cần thiết quá lớn, có thể dẫn đến tình trạng quá tải bộ nhớ GPU; đồng thời, quá trình huấn luyện cũng đòi hỏi các chuỗi dữ liệu có độ dài rất lớn. Những yếu tố này khiến việc xử lý hình ảnh trở nên chậm chạp hơn.

<|ref|>sub_title<|/ref|><|det|>[[117, 647, 362, 663]]<|/det|>
### 2.2. Các mô hình OCR hoạt động theo nguyên lý từ đầu đến cuối

<|ref|>text<|/ref|><|det|>[[115, 673, 882, 899]]<|/det|>  
Việc nhận dạng văn bản từ hình ảnh, đặc biệt là các công việc phân tích nội dung tài liệu, luôn là một lĩnh vực được quan tâm sâu rộng trong lĩnh vực chuyển đổi hình ảnh thành văn bản. Với sự phát triển của các mô hình trí tuệ nhân tạo, ngày càng nhiều mô hình OCR hoạt động theo nguyên lý “từ đầu đến cuối” đã xuất hiện, thay đổi căn bản cấu trúc truyền thống (vốn yêu cầu sử dụng các mô hình riêng biệt để phát hiện và nhận diện thông tin) bằng cách đơn giản hóa quy trình xử lý. Nougat [6] là người đầu tiên áp dụng cấu trúc này cho việc nhận dạng văn bản trong các bài báo khoa học trên arXiv, chứng minh tiềm năng của các mô hình này trong việc xử lý các nhiệm vụ phức tạp liên quan đến nhận thức hình ảnh. GOT-OCR2.0 [38] mở rộng phạm vi ứng dụng của OCR2.0 sang nhiều loại tác vụ phân tích hình ảnh hơn, đồng thời thiết kế các mô hình OCR với sự cân bằng giữa hiệu suất và tính hiệu quả, từ đó làm nổi bật thêm tiềm năng của các nghiên cứu về OCR theo nguyên lý “từ đầu đến cuối”. Ngoài ra, các mô hình nhận thức hình ảnh tổng quát như loạt Qwen-VL [35], InternVL [8] và nhiều phiên bản phái sinh của chúng cũng liên tục được cải thiện về khả năng nhận dạng văn bản từ hình ảnh, giúp mở rộng giới hạn của các công nghệ này. Tuy nhiên, vẫn còn một câu hỏi quan trọng mà các mô hình hiện tại chưa giải đáp được: Đối với một tài liệu gồm 1000 từ, ít nhất cần bao nhiêu thông tin hình ảnh là đủ để thực hiện quá trình nhận dạng văn bản? Câu hỏi này có ý nghĩa quan trọng đối với các nghiên cứu liên quan đến nguyên tắc “Một hình ảnh giá trị bằng ngàn lời nói”.

============================================================
--- Trang 5 ---
============================================================

![Hình 0_0](images/page_5_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 260, 881, 327]]<|/thông tin chi tiết|>
<center>Hình 3 | Cấu trúc của DeepSeek-OCR. DeepSeek-OCR bao gồm một bộ mã hóa sâu (DeepEncoder) và một bộ giải mã sâu DeepSeek-3B-MoE. DeepEncoder là thành phần cốt lõi của DeepSeek-OCR, bao gồm ba thành phần chính: công cụ SAM [17] dùng để thu thập thông tin dựa trên cơ chế chú ý theo khung cửa sổ; công cụ CLIP [29] dùng để tích hợp kiến thức từ các nguồn khác nhau thông qua cơ chế chú ý toàn diện; và một bộ nén dữ liệu có kích thước \(16\times\) token, đóng vai trò kết nối các thành phần này lại với nhau.</center>

<|ref|>sub_title<|/ref|><|det|>[[116, 350, 279, 368]]<|/det|>
## 3. Phương pháp tiếp cận</td>

<|ref|>sub_title<|/ref|><|det|>[[116, 382, 259, 398]]<|/det|>
### 3.1. Kiến trúc</td>

<|ref|>text<|/ref|><|det|>[[115, 408, 882, 540]]<|/det|>  
Như được minh họa trong Hình 3, DeepSeek-OCR sử dụng một kiến trúc VLM tích hợp từ đầu đến cuối, bao gồm cả bộ mã hóa và bộ giải mã. Bộ mã hóa (tên là DeepEncoder) có nhiệm vụ trích xuất các đặc điểm hình ảnh, chuyển đổi chúng thành dạng “token” và sau đó nén chúng lại. Bộ giải mã được sử dụng để tạo ra kết quả mong muốn dựa trên các “token” hình ảnh và các thông tin hướng dẫn được cung cấp. DeepEncoder chứa khoảng 380 triệu tham số, được cấu tạo chủ yếu từ mô-đun SAM có dung lượng 80 triệu tham số [17] và mô-đun CLIP có dung lượng 300 triệu tham số [29], được kết nối liên tiếp với nhau. Bộ giải mã sử dụng kiến trúc MoE có 3 tỷ tham số hoạt động [19, 20], với tổng số 570 triệu tham số được sử dụng trong quá trình xử lý dữ liệu. Trong các phần tiếp theo, chúng ta sẽ tìm hiểu chi tiết hơn về các thành phần cấu tạo của mô hình này, quy trình xử lý dữ liệu và các kỹ thuật huấn luyện mô hình.

<|ref|>sub_title<|/ref|><|det|>[[116, 562, 267, 578]]<|/det|>
### 3.2. DeepEncoder

<|ref|>text<|/ref|><|det|>[[116, 588, 882, 668]]<|/det|>  
Để nghiên cứu khả năng áp dụng phương pháp nén dữ liệu hình ảnh dựa trên ngữ cảnh, chúng ta cần một bộ mã hóa hình ảnh có những đặc điểm sau: 1. Có khả năng xử lý các độ phân giải cao; 2. Tiêu thụ ít tài nguyên khi xử lý độ phân giải cao; 3. Sử dụng ít thông tin đại diện cho hình ảnh; 4. Hỗ trợ các đầu vào có độ phân giải khác nhau; 5. Có số lượng tham số vừa phải. Tuy nhiên, như đã mô tả ở Phần 2.1, các bộ mã hóa mã nguồn mở hiện có không thể đáp ứng đầy đủ tất cả các yêu cầu trên. Do đó, chúng tôi đã tự thiết kế một bộ mã hóa hình ảnh mới, có tên là DeepEncoder.

<|ref|>title<|/ref|><|det|>[[117, 688, 400, 704]]<|/det|>
#### 3.2.1. Cấu trúc của DeepEncoder

<|ref|>text<|/ref|><|det|>[[115, 714, 882, 891]]<|/det|>  
DeepEncoder chủ yếu bao gồm hai thành phần: một thành phần trích xuất các đặc điểm liên quan đến khả năng nhận diện hình ảnh, được điều khiển bởi thuật toán chú ý theo cửa sổ; và một thành phần trích xuất các đặc điểm kiến thức hình ảnh, sử dụng thuật toán chú ý toàn cục. Để tận dụng những lợi ích từ các nghiên cứu trước đây về việc huấn luyện sơ bộ, chúng tôi lựa chọn SAM-base (kích thước khối dữ liệu 16) và CLIP-large làm cấu trúc chính cho hai thành phần này. Đối với CLIP, chúng tôi loại bỏ lớp đưa dữ liệu vào dạng khối đầu tiên, vì đầu vào của nó không còn là hình ảnh nữa mà là các mã hóa từ các quá trình xử lý trước đó. Giữa hai thành phần này, chúng tôi áp dụng mô-đun hội tụ 2 lớp theo phương pháp Vary [36] để thực hiện việc giảm kích thước các mã hóa hình ảnh xuống còn \(16\times\). Mỗi lớp hội tụ có kích thước kernel là 3, bước chuyển động là 2, độ đầy là 1, và số kênh tín hiệu tăng từ 256 lên 1024. Nếu chúng ta đưa vào một hình ảnh có kích thước \(1024 \times 1024\), DeepEncoder sẽ chia nó thành \(1024 / 16 \times 1024 / 16 = 4096\) mã hóa hình ảnh. Vì nửa đầu của hệ thống này chủ yếu sử dụng thuật toán chú ý theo cửa sổ và chỉ tốn bộ nhớ 80MB, nên mức độ kích hoạt của các thành phần này vẫn được coi là chấp nhận được. Trước khi các mã hóa này được đưa vào quá trình xử lý bằng thuật toán chú ý toàn cục…

============================================================
--- Trang 6 ---
============================================================

![Hình ảnh 0_0](images/page_6_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 269, 881, 318]]<|/thông tin chi tiết|>
<center>Hình 4: Để kiểm tra hiệu suất của mô hình ở các tỷ lệ nén khác nhau (đòi hỏi số lượng “token hình ảnh” khác nhau) và nâng cao tính ứng dụng thực tế của DeepSeek-OCR, chúng tôi đã cấu hình nó với nhiều chế độ độ phân giải khác nhau.</center>

<|ref|>text<|/ref|><|det|>[[115, 342, 881, 376]]<|/det|>
the 4096 tokens go through the compression module and the token count becomes \(4096 / 16 = 256\), thus making the overall activation memory controllable.<|ref|>text<|/ref|><|det|>[[115, 342, 881, 376]]<|/det|>  
4096 ký hiệu này được đưa qua mô-đun nén; sau đó, số lượng các ký hiệu này giảm xuống còn \(4096 \div 16 = 256\). Nhờ vậy, tổng dung lượng bộ nhớ cần thiết để xử lý dữ liệu trở nên có thể kiểm soát được.

<|ref|>biểu bảng<|/ref|><|thông tin|>[[166, 431, 829, 535]]<|/thông tin|>
<|ref|>chú thích biểu bảng<|/ref|><|thông tin|>[[115, 386, 881, 420]]<|/thông tin|>
Bảng 1 | Khả năng hỗ trợ nhiều độ phân giải của DeepEncoder. Vì mục đích nghiên cứu lẫn ứng dụng, chúng tôi đã thiết kế DeepEncoder với nhiều độ phân giải khác nhau và các chế độ điều chỉnh độ phân giải một cách linh hoạt.

<table><tr><td rowspan="2">Chế độ</td><td colspan="4">Độ phân giải gốc</td><td colspan="2">Độ phân giải động</td></tr><tr><td>Tiny</td><td>Small</td><td>Base</td><td>Large</td><td>Gundam</td><td>Gundam-M</td></tr><tr><td>Độ phân giải</td><td>512</td><td>640</td><td>1024</td><td>1280</td><td>640+1024</td><td>1024+1280</td></tr><tr><td>Số khối điểm ảnh</td><td>64</td><td>100</td><td>256</td><td>400</td><td>n×100+256</td><td>n×256+400</td></tr><tr><td>Quy trình xử lý hình ảnh</td><td colspan="3">Thay đổi kích thước hình ảnh + tăng/không gian viền</td><td colspan="3">Thay đổi kích thước hình ảnh + tăng/không gian viền</td></tr></table>

<|ref|>title<|/ref|><|det|>[[117, 560, 396, 576]]<|/det|>
#### 3.2.2. Hỗ trợ nhiều độ phân giải khác nhau

<|ref|>text<|/ref|><|det|>[[115, 586, 881, 636]]<|/det|>  
Giả sử chúng ta có một hình ảnh chứa 1000 ký tự quang học và muốn kiểm tra xem cần bao nhiêu “token thị giác” để giải mã hình ảnh đó. Điều này đòi hỏi mô hình phải hỗ trợ việc sử dụng một số lượng khác nhau các “token thị giác”; nói cách khác, bộ mã hóa sâu (DeepEncoder) cần phải hỗ trợ nhiều độ phân giải khác nhau.

<|ref|>text<|/ref|><|det|>[[115, 642, 881, 725]]<|/det|>  
Chúng tôi đã đáp ứng được yêu cầu nêu trên thông qua phương pháp giải quyết động dựa trên các mã hóa vị trí, đồng thời thiết kế nhiều chế độ độ phân giải khác nhau để thực hiện việc huấn luyện mô hình đồng thời, nhằm đảm bảo rằng một mô hình DeepSeek-OCR duy nhất có thể hỗ trợ nhiều độ phân giải khác nhau. Như được minh họa trong Hình 4, DeepEncoder chủ yếu hỗ trợ hai chế độ đầu vào chính: độ phân giải gốc và độ phân giải động. Mỗi chế độ đều bao gồm nhiều tiểu chế độ con khác nhau.

<|ref|>text<|/ref|><|det|>[[115, 731, 881, 844]]<|/det|>  
Độ phân giải gốc hỗ trợ bốn chế độ con: Tiny, Small, Base và Large, với các độ phân giải và số lượng “token” tương ứng là \(512 \times 512\) (64), \(640 \times 640\) (100), \(1024 \times 1024\) (256) và \(1280 \times 1280\) (400). Vì các mô hình Tiny và Small có độ phân giải tương đối thấp, để tránh lãng phí các “token” xử lý hình ảnh, các hình ảnh này được điều chỉnh kích thước trực tiếp mà không thay đổi tỷ lệ khung hình ban đầu. Đối với các chế độ Base và Large, để bảo toàn tỷ lệ khung hình gốc, các hình ảnh sẽ được điền thêm ký tự để đạt đến kích thước mong muốn. Sau khi điền thêm ký tự, số lượng “token” hợp lệ sẽ ít hơn số lượng “token” thực tế; công thức tính toán số lượng “token” hợp lệ như sau:

<|ref|>phương trình<|/ref|><|det|>[[250, 855, 880, 874]]<|/det|>
\[N_{hợp lệ} = \lceil N_{thực tế} \times \left[1 - \left(\frac{max(w,h) - min(w,h)}{max(w,h)}\right)\right]\rceil \quad (1)\]

<|ref|>text<|/ref|><|det|>[[115, 885, 716, 902]]<|/det|>  
Trong đó, \(w\) và \(h\) lần lượt là độ rộng và độ cao của hình ảnh đầu vào ban đầu.

============================================================
--- Trang 7 ---
============================================================

<|ref|>text<|/ref|><|det|>[[115, 100, 883, 262]]<|/det|>
Dynamic resolution can be composed of two native resolutions. For example, Gundam mode consists of \(n \times 640 \times 640\) tiles (local views) and a \(1024 \times 1024\) global view. The tiling method following InternVL2.0 [8]. Supporting dynamic resolution is mainly for application considerations, especially for ultra- high- resolution inputs (such as newspaper images). Tiling is a form of secondary window attention that can effectively reduce activation memory further. It's worth noting that due to our relatively large native resolutions, images won't be fragmented too much under dynamic resolution (the number of tiles is controlled within the range of 2 to 9). The vision token number output by the DeepEncoder under Gundam mode is: \(n \times 100 + 256\), where \(n\) is the number of tiles. For images with both width and height smaller than 640, \(n\) is set to 0, i.e., Gundam mode will degrade to Base mode.<|ref|>text<|/ref|><|det|>[[115, 100, 883, 262]]<|/det|>  
Độ phân giải động có thể được tạo thành từ hai độ phân giải gốc khác nhau. Ví dụ, chế độ Gundam bao gồm các ô hình ảnh có kích thước \(n \times 640 \times 640\) và một hình ảnh tổng thể có kích thước \(1024 \times 1024\). Phương pháp sắp xếp các ô này tuân theo tiêu chuẩn InternVL2.0 [8]. Việc hỗ trợ độ phân giải động chủ yếu nhằm phục vụ các ứng dụng cụ thể, đặc biệt là đối với các nguồn dữ liệu có độ phân giải siêu cao (chẳng hạn như hình ảnh trên báo chí). Phương pháp này giúp giảm đáng kể lượng bộ nhớ cần thiết để xử lý dữ liệu hình ảnh. Đáng chú ý là do độ phân giải gốc của chúng ta khá lớn, nên khi sử dụng độ phân giải động, hình ảnh không bị phân mảnh quá nhiều (số lượng các ô hình ảnh được kiểm soát trong khoảng từ 2 đến 9). Số lượng các “token hình ảnh” được tạo ra bởi thuật toán DeepEncoder trong chế độ Gundam là \(n \times 100 + 256\), trong đó \(n\) là số lượng các ô hình ảnh. Đối với những hình ảnh có chiều rộng và chiều cao nhỏ hơn 640, giá trị của \(n\) sẽ được đặt thành 0; trong trường hợp này, chế độ Gundam sẽ tự động chuyển sang chế độ Base.

<|ref|>text<|/ref|><|det|>[[115, 270, 883, 350]]<|/det|>  
Chế độ Gundam được huấn luyện cùng với bốn chế độ độ phân giải khác nhau nhằm mục đích tạo ra một mô hình có thể hỗ trợ nhiều độ phân giải khác nhau. Lưu ý rằng chế độ Gundam-Master (gồm 115×1024 điểm ảnh cục bộ + 1280×1280 điểm ảnh toàn cảnh) được xây dựng thông qua việc tiếp tục huấn luyện trên mô hình DeepSeek-OCR đã được đào tạo trước đó. Việc này chủ yếu nhằm đảm bảo sự cân bằng trong quá trình huấn luyện; bởi vì độ phân giải của chế độ Gundam-Master quá lớn, và việc huấn luyện nó cùng với các chế độ khác sẽ làm chậm tốc độ tổng thể của quá trình đào tạo.

<|ref|>sub_title<|/ref|><|det|>[[115, 372, 306, 388]]<|/det|>
### 3.3. Bộ giải mã MoE

<|ref|>text<|/ref|><|det|>[[115, 398, 883, 480]]<|/det|>  
Bộ giải mã của chúng tôi sử dụng công nghệ DeepSeekMoE [19, 20], cụ thể là mô hình DeepSeek-3B-MoE. Trong quá trình thực hiện các phép tính dự đoán, mô hình này kích hoạt 6 trong tổng số 64 mô-đun chuyên biệt và 2 mô-đun chung, với khoảng 570 triệu tham số được sử dụng trong quá trình tính toán. Mô hình DeepSeekMoE 3B rất phù hợp cho các nghiên cứu về các hệ thống trí tuệ nhân tạo tập trung vào từng lĩnh vực cụ thể (chẳng hạn như công nghệ nhận diện chữ viết tay), bởi vì nó vừa giữ được khả năng xử lý thông tin mạnh mẽ của các mô hình có dung lượng lớn, vừa sở hữu hiệu suất tính toán cao như các mô hình nhỏ hơn.

<|ref|>text<|/ref|><|det|>[[115, 488, 880, 520]]<|/det|>  
Bộ giải mã sẽ tái tạo lại dạng biểu diễn văn bản gốc từ các mã hóa ẩn chứa được tạo ra bởi DeepEncoder như sau:

<|ref|>phương trình<|/ref|><|det|>[[278, 530, 880, 550]]<|/det|>
\[f_{\mathrm{dec}}:\mathbb{R}^{n\times d_{\mathrm{latent}}}\to \mathbb{R}^{N\times d_{\mathrm{text}}}; \quad \hat{\mathbf{X}} = f_{\mathrm{dec}}(\mathbf{Z})\quad \text{trong đó} n\leq N \quad (2)\]

<|ref|>text<|/ref|><|det|>[[115, 560, 881, 643]]<|/det|>  
Trong đó, \(\mathbf{Z} \in \mathbb{R}^{n \times d_{\mathrm{latent}}}\) là các token ẩn được nén ra từ mô hình DeepEncoder, còn \(\hat{\mathbf{X}} \in \mathbb{R}^{N \times d_{\mathrm{text}}}\) là biểu diễn văn bản được tái tạo lại. Hàm \(f_{\mathrm{dec}}\) đại diện cho một phép ánh xạ phi tuyến tính; phép ánh xạ này có thể được học một cách hiệu quả thông qua các mô hình ngôn ngữ được huấn luyện theo phương pháp OCR. Có thể suy đoán rằng các mô hình LLM, nhờ vào các quá trình tối ưu hóa huấn luyện chuyên biệt, sẽ thể hiện khả năng tích hợp những công nghệ này một cách tự nhiên hơn.

<|ref|>sub_title<|/ref|><|det|>[[115, 667, 258, 682]]<|/det|>
### 3.4. Máy chạy dữ liệu

<|ref|>text<|/ref|><|det|>[[115, 692, 883, 790]]<|/det|>  
Chúng tôi đã xây dựng những bộ dữ liệu huấn luyện phức tạp và đa dạng cho hệ thống DeepSeek-OCR, bao gồm:  
– Dữ liệu OCR 1.0, chủ yếu bao gồm các nhiệm vụ OCR truyền thống như nhận diện văn bản trong hình ảnh hay tài liệu;  
– Dữ liệu OCR 2.0, tập trung vào việc phân tích các hình ảnh nhân tạo phức tạp, chẳng hạn như biểu đồ thông dụng, công thức hóa học hay cấu trúc hình học;  
– Dữ liệu thị giác tổng quát, nhằm trang bị cho DeepSeek-OCR khả năng hiểu biết về hình ảnh một cách tổng quát hơn, đồng thời giữ nguyên giao diện thị giác cơ bản của hệ thống.

<|ref|>title<|/ref|><|det|>[[115, 810, 279, 825]]<|/det|>
#### Dữ liệu OCR 1.0

<|ref|>text<|/ref|><|det|>[[115, 835, 881, 900]]<|/det|>  
Dữ liệu tài liệu là ưu tiên hàng đầu đối với công cụ DeepSeek-OCR. Chúng tôi đã thu thập được 30 triệu trang tài liệu dạng PDF đa dạng ngôn ngữ từ Internet; trong đó, các tài liệu bằng tiếng Trung và tiếng Anh chiếm khoảng 25 triệu trang, còn các ngôn ngữ khác chiếm 5 triệu trang. Đối với những dữ liệu này, chúng tôi đã tạo ra hai loại ghi chú chuẩn xác: ghi chú sơ lược và ghi chú chi tiết. Các ghi chú sơ lược được rút ra từ dữ liệu thu thập được…

============================================================
--- Trang 8 ---
============================================================

![Hình ảnh 0_0](images/page_8_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin|>[[115, 454, 881, 503]]<|/thông tin|>
<center>Hình 5 | Các ghi chú chi tiết từ công cụ OCR 1.0 được hiển thị ở đây. Chúng tôi đã định dạng dữ liệu tham chiếu theo dạng xen kẽ giữa các đoạn văn bản và thông tin địa lý; trước mỗi đoạn văn bản đều được ghi rõ tọa độ và nhãn của nó trong hình ảnh gốc. Tất cả các tọa độ đều được quy đổi sang khoảng từ 0 đến 1000.</center>

<|ref|>text<|/ref|><|det|>[[115, 526, 882, 737]]<|/det|>  
Dữ liệu này được thu thập trực tiếp từ tập dữ liệu đầy đủ bằng công cụ fitz, với mục đích huấn luyện mô hình nhằm giúp nó nhận diện văn bản được hiển thị trên màn hình, đặc biệt là các văn bản được viết bằng các ngôn ngữ thiểu số. Các bộ ghi chú chi tiết bao gồm 2 triệu trang văn bản tiếng Trung và tiếng Anh; chúng được đánh dấu bằng các mô hình bố cục tiên tiến (như PP-DocLayout [33]) và các công cụ OCR (như MinuerU [34] và GOT-OCR2.0 [38]) để tạo ra dữ liệu phục vụ cho quá trình nhận diện. Đối với các ngôn ngữ thiểu số, trong phần xác định cấu trúc văn bản, chúng tôi nhận thấy rằng các mô hình bố cục này có khả năng tổng quát hóa tốt. Trong phần nhận diện văn bản, chúng tôi sử dụng công cụ fitz để tạo ra các đoạn văn bản nhỏ để huấn luyện mô hình GOT-OCR2.0; sau đó, dùng mô hình đã được huấn luyện này để đánh dấu các đoạn văn bản sau khi chúng được xử lý về mặt bố cục, từ đó tạo ra 600.000 mẫu dữ liệu. Trong quá trình huấn luyện mô hình DeepSeek-OCR, các nhãn đánh dấu cơ bản và chi tiết được sử dụng các thông tin khác nhau để phân biệt. Các cặp hình ảnh kèm văn bản được sử dụng để đánh giá chất lượng của các bộ ghi chú chi tiết có thể được xem ở Hình 5. Chúng tôi cũng thu thập thêm 3 triệu bộ dữ liệu văn bản, từ đó tạo ra các cặp hình ảnh-không-gian văn bản chất lượng cao mà không cần thông tin về bố cục văn bản; những dữ liệu này đặc biệt hữu ích đối với các công thức toán học và các bảng biểu định dạng HTML. Ngoài ra, chúng tôi cũng sử dụng một số tài nguyên mã nguồn mở [28, 37] như tài liệu bổ sung cho quá trình nghiên cứu này.

<|ref|>text<|/ref|><|det|>[[116, 743, 881, 810]]<|/det|>  
Đối với công nghệ nhận dạng ký tự trong hình ảnh các cảnh vật tự nhiên, mô hình của chúng tôi hỗ trợ chủ yếu tiếng Trung và tiếng Anh. Các nguồn dữ liệu hình ảnh được lấy từ LAION [31] và Wukong [13], và đã được đánh dấu bằng công cụ PaddleOCR [9]; mỗi nguồn chứa 10 triệu mẫu dữ liệu dành cho tiếng Trung và tiếng Anh. Tương tự như công nghệ nhận dạng ký tự trong tài liệu, công nghệ này cũng cho phép người dùng điều khiển việc có hiển thị các khung xác định vị trí ký tự hay không thông qua các lệnh chỉ đạo cụ thể.

<|ref|>title<|/ref|><|det|>[[116, 828, 280, 844]]<|/det|>
#### Dữ liệu OCR 2.0

<|ref|>text<|/ref|><|det|>[[115, 854, 881, 887]]<|/det|>  
Theo tiêu chuẩn GOT-OCR2.0 [38], chúng tôi coi dữ liệu biểu đồ, công thức hóa học và thông tin liên quan đến hình học phẳng là dữ liệu OCR 2.0. Đối với dữ liệu biểu đồ, theo hướng dẫn của OneChart [7], chúng tôi sử dụng các thư viện pyecharts và matplotlib để xử lý dữ liệu này.

============================================================
--- Trang 9 ---
============================================================

![Hình 0_0](images/page_9_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 240, 881, 321]]<|/thông tin chi tiết|>
<center>Hình 6: Đối với các biểu đồ, chúng tôi không sử dụng định dạng từ điển [7] của công cụ OneChart, mà thay vào đó sử dụng định dạng bảng HTML cho các tiêu đề biểu đồ; cách này giúp tiết kiệm được một lượng lớn dung lượng lưu trữ. Đối với các đối tượng hình học phẳng, chúng tôi chuyển đổi dữ liệu thực tế thành định dạng từ điển, trong đó các khóa bao gồm tên các đoạn thẳng, tọa độ hai đầu mút của đoạn thẳng, loại đoạn thẳng, v.v., nhằm tăng tính dễ đọc. Mỗi đoạn thẳng đều được mã hóa theo phương pháp Slow Perception [39].</center>

<|ref|>text<|/ref|><|det|>[[115, 345, 882, 508]]<|/det|>  
Để hiển thị 10 triệu hình ảnh, chủ yếu bao gồm các loại biểu đồ dạng đường thẳng, thanh, phần trăm và biểu đồ tổng hợp thường được sử dụng, chúng tôi coi việc xử lý dữ liệu biểu đồ là quá trình chuyển đổi các hình ảnh đó thành các bảng dữ liệu dạng HTML, như được minh họa trong Hình 6(a). Đối với các công thức hóa học, chúng tôi sử dụng định dạng SMILES từ PubChem làm nguồn dữ liệu và sử dụng công cụ RDKit để chuyển đổi chúng thành hình ảnh, tạo ra tổng cộng 5 triệu cặp dữ liệu hình ảnh-không gian văn bản. Đối với các hình ảnh hình học phẳng, chúng tôi áp dụng phương pháp Slow Perception [39] để tạo ra chúng; cụ thể, chúng tôi sử dụng kích thước “thước đo” là 4 để mô hình hóa từng đoạn thẳng trong hình ảnh. Nhằm tăng đa dạng của dữ liệu được hiển thị, chúng tôi cũng áp dụng phương pháp tăng cường dữ liệu dựa trên nguyên lý bất biến hình học; cụ thể, cùng một hình ảnh hình học sẽ được dịch chuyển theo các hướng khác nhau so với vị trí ban đầu, sao cho điểm đầu và điểm cuối của đoạn thẳng vẫn nằm tại cùng một vị trí trong hệ tọa độ. Dựa trên các phương pháp này, chúng tôi đã tạo ra tổng cộng 1 triệu bộ dữ liệu hình học phẳng, như được minh họa trong Hình 6(b).

<|ref|>title<|/ref|><|det|>[[117, 527, 330, 543]]<|/det|>
#### 3.4.3. Dữ liệu hình ảnh tổng quát

<|ref|>text<|/ref|><|det|>[[116, 553, 881, 666]]<|/det|>  
DeepEncoder có thể hưởng lợi từ những kết quả đạt được trong quá trình huấn luyện sơ bộ của CLIP, đồng thời cũng sở hữu đủ số lượng tham số để tiếp nhận các kiến thức thị giác tổng quát. Do đó, chúng tôi cũng đã chuẩn bị một số dữ liệu phù hợp cho DeepSeek-OCR. Theo hướng dẫn của DeepSeek-VL2 [40], chúng tôi đã tạo ra các dữ liệu liên quan đến các nhiệm vụ như việc gán chú thích cho hình ảnh, phát hiện đối tượng và xác định mối quan hệ giữa các đối tượng trong hình ảnh. Lưu ý rằng DeepSeek-OCR không phải là một mô hình VLM tổng quát; phần dữ liệu này chỉ chiếm khoảng \(20\%\) tổng lượng dữ liệu tổng thể. Chúng tôi cung cấp loại dữ liệu này chủ yếu nhằm bảo đảm tính tổng quát của công cụ thị giác này, giúp các nhà nghiên cứu quan tâm đến mô hình của chúng tôi và các nhiệm vụ thị giác nói chung có thể tiếp tục phát triển công trình nghiên cứu của mình một cách thuận lợi trong tương lai.

<|ref|>title<|/ref|><|det|>[[117, 686, 288, 702]]<|/det|>
#### 3.4.4. Dữ liệu chỉ chứa văn bản

<|ref|>text<|/ref|><|det|>[[117, 712, 881, 777]]<|/det|>
To ensure the model's language capabilities, we introduced \(10\%\) of in- house text- only pretrain data, with all data processed to a length of 8192 tokens, which is also the sequence length for DeepSeek- OCR. In summary, when training DeepSeek- OCR, OCR data accounts for \(70\%\), general vision data accounts for \(20\%\), and text- only data accounts for \(10\%\).<|ref|>text<|/ref|><|det|>[[117, 712, 881, 777]]<|/det|>  
Để đảm bảo khả năng xử lý ngôn ngữ của mô hình, chúng tôi đã sử dụng 10% dữ liệu được huấn luyện trước chỉ chứa văn bản, trong đó tất cả các dữ liệu đều được xử lý sao cho có độ dài bằng 8192 ký tự – đây cũng chính là độ dài chuỗi dữ liệu được sử dụng trong DeepSeek-OCR. Nói chung, khi huấn luyện DeepSeek-OCR, dữ liệu OCR chiếm 70%, dữ liệu thị giác thông thường chiếm 20%, và dữ liệu chỉ chứa văn bản chiếm 10%.

<|ref|>sub_title<|/ref|><|det|>[[117, 800, 309, 817]]<|/det|>
### 3.5. Quy trình đào tạo mô hình</td>

<|ref|>text<|/ref|><|det|>[[117, 827, 881, 891]]<|/det|>  
Quy trình đào tạo của chúng tôi rất đơn giản và bao gồm hai giai đoạn chính: a) Đào tạo riêng bộ công cụ DeepEncoder; b) Đào tạo hệ thống DeepSeek-OCR. Lưu ý rằng chế độ “Gundam-master” được tạo ra bằng cách tiếp tục đào tạo mô hình DeepSeek-OCR đã được huấn luyện sẵn, sử dụng 6 triệu dữ liệu mẫu. Vì quy trình đào tạo này giống hệt với các chế độ khác, chúng tôi sẽ không trình bày chi tiết thêm ở đây.

============================================================
--- Trang 10 ---
============================================================

<|ref|>title<|/ref|><|det|>[[115, 101, 348, 116]]<|/det|>
#### 3.5.1. Đào tạo mô hình DeepEncoder

<|ref|>text<|/ref|><|det|>[[115, 127, 881, 207]]<|/det|>  
3.5.1. Đào tạo DeepEncoder  
Theo phương pháp được đề xuất trong [36], chúng tôi sử dụng một mô hình ngôn ngữ gọn nhẹ [15] và áp dụng cấu trúc dự đoán các ký tự tiếp theo để đào tạo DeepEncoder. Trong giai đoạn này, chúng tôi sử dụng toàn bộ dữ liệu từ các bộ dữ liệu OCR 1.0 và 2.0 đã nêu trên, cùng với 100 triệu dữ liệu thông thường được lấy mẫu từ bộ dữ liệu LAION [31]. Tất cả các dữ liệu này đều được sử dụng để đào tạo trong 2 chu kỳ, với kích thước mỗi lần xử lý là 1280 dữ liệu. Chúng tôi áp dụng thuật toán tối ưu hóa AdamW [23] kết hợp với lịch trình điều chỉnh tốc độ học máy loại cosine annealing [22], với tốc độ học máy được đặt ở mức 5e-5. Độ dài chuỗi dữ liệu được sử dụng để đào tạo là 4096.

<|ref|>title<|/ref|><|det|>[[117, 226, 368, 242]]<|/det|>
#### 3.5.2. Đào tạo DeepSeek-OCR

<|ref|>text<|/ref|><|det|>[[115, 252, 881, 430]]<|/det|>  
Sau khi hoàn thành việc xây dựng công cụ DeepEncoder, chúng tôi sử dụng dữ liệu được đề cập ở Phần 3.4 để huấn luyện mô hình DeepSeek-OCR. Toàn bộ quá trình huấn luyện được thực hiện trên nền tảng HAI-LLM [14]. Mô hình này áp dụng phương pháp song song hóa dữ liệu và được chia thành 4 phần: DeepEncoder chiếm 2 phần, còn bộ giải mã chiếm 2 phần còn lại. Đối với phần DeepEncoder, chúng tôi coi các thành phần SAM và bộ nén dữ liệu như những công cụ xử lý văn bản, đặt chúng vào luồng xử lý PP0 và không thay đổi các tham số của chúng trong quá trình huấn luyện; trong khi đó, phần CLIP được xem là lớp đầu vào dùng để xử lý dữ liệu ngôn ngữ và được đặt vào luồng xử lý PP1, với các tham số có thể được điều chỉnh trong quá trình huấn luyện. Đối với phần mô hình ngôn ngữ, vì DeepSeek3B-MoE gồm 12 lớp, chúng tôi chia 6 lớp cho mỗi trong hai luồng xử lý PP2 và PP3. Chúng tôi sử dụng 20 node (mỗi node được trang bị 8 GPU loại A100-40G) để thực hiện quá trình huấn luyện, với mức độ song song hóa dữ liệu là 40 và kích thước mỗi lô dữ liệu là 640. Chúng tôi sử dụng thuật toán tối ưu hóa AdamW, kèm theo lịch trình huấn luyện dựa trên số bước và tỷ lệ học tập ban đầu là 3e-5. Đối với dữ liệu chỉ chứa văn bản, tốc độ huấn luyện là 90 tỷ token mỗi ngày; còn đối với dữ liệu đa phương thức, tốc độ huấn luyện là 70 tỷ token mỗi ngày.

<|ref|>text<|/ref|><|det|>[[115, 441, 881, 523]]<|/det|>
Bảng 2: Chúng tôi đã kiểm tra tỷ lệ nén văn bản giữa hình ảnh và văn bản khi sử dụng công cụ DeepSeek-OCR, bằng cách sử dụng tất cả các tài liệu tiếng Anh có độ dài từ 600 đến 1300 ký tự trong bộ dữ liệu đánh giá của Fox [21]. Các ký tự văn bản được tính dựa trên số lượng ký tự sau khi văn bản gốc được phân tích bằng công cụ tokenizer của DeepSeek-OCR. Số lượng ký tự hình ảnh lần lượt là 64 hoặc 100, tùy thuộc vào việc hình ảnh đầu vào được điều chỉnh kích thước thành 512x512 hay 640x640 trước khi được xử lý bởi công cụ DeepEncoder.

<|ref|>bảng</|/ref|><|det|>[[211, 533, 784, 700]]</|/det|>

<table><tr><td rowspan="2">Các ký hiệu văn bản</td><td colspan="2">Số lượng ký hiệu hình ảnh = 64</td><td colspan="2">Số lượng ký hiệu hình ảnh = 100</td></tr><tr><td>Độ chính xác</td><td>Mức độ nén dữ liệu</td><td>Độ chính xác</td><td>Mức độ nén dữ liệu</td></tr><tr><td>600–700</td><td>96,5%</td><td>10,5 lần</td><td>98,5%</td><td>6,7 lần</td></tr><tr><td>700–800</td><td>93,8%</td><td>11,8 lần</td><td>97,3%</td><td>7,5 lần</td></tr><tr><td>800–900</td><td>83,8%</td><td>13,2 lần</td><td>96,8%</td><td>8,5 lần</td></tr><tr><td>900–1000</td><td>85,9%</td><td>15,1 lần</td><td>96,8%</td><td>9,7 lần</td></tr><tr><td>1000–1100</td><td>79,3%</td><td>16,5 lần</td><td>91,5%</td><td>10,6 lần</td></tr><tr><td>1100–1200</td><td>76,4%</td><td>17,7 lần</td><td>89,8%</td><td>11,3 lần</td></tr><tr><td>1200–1300</td><td>59,1%</td><td>19,7 lần</td><td>87,1%</td><td>12,6 lần</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 729, 253, 746]]<|/det|>
## 4. Đánh giá

<|ref|>sub_title<|/ref|><|det|>[[117, 761, 416, 777]]<|/det|>
### 4.1. Nghiên cứu về việc nén dữ liệu hình ảnh kết hợp văn bản

<|ref|>text<|/ref|><|det|>[[115, 788, 881, 900]]<|/det|>  
4. Đánh giá  
4.1. Nghiên cứu về việc nén dữ liệu văn bản kết hợp hình ảnh  
Chúng tôi sử dụng các bài kiểm thử của Fox [21] để đánh giá khả năng nén và giải nén dữ liệu văn bản của công cụ DeepSeek-OCR, nhằm khám phá trước tiên tính khả thi và các hạn chế của phương pháp nén dữ liệu này. Chúng tôi lấy phần văn bản tiếng Anh trong tập dữ liệu Fox làm đối tượng thử nghiệm, tiến hành phân tích cấu trúc văn bản bằng công cụ tokenizer của DeepSeek-OCR (với bộ từ vựng gồm khoảng 129.000 từ), và chọn những tài liệu có số lượng từ từ 600 đến 1.300 để thử nghiệm – tương ứng với khoảng 100 trang văn bản. Vì số lượng từ trong các tài liệu này không quá lớn, chúng tôi chỉ cần kiểm tra hiệu suất của công cụ ở hai chế độ: “Tiny” (64 từ) và “Small” (100 từ). Chúng tôi sử dụng đoạn mã sau làm ví dụ để thực hiện thử nghiệm:

============================================================
--- Trang 11 ---
============================================================

<|ref|>bảng</|/ref|><|det|>[[120, 207, 875, 707]]</|/det|>
<|ref|>chú thích bảng</|/ref|><|det|>[[115, 99, 881, 197]]</|/det|>
Bảng 3: Chúng tôi sử dụng công cụ OmniDocBench [27] để đánh giá hiệu suất của mô hình DeepSeek-OCR trong các tác vụ phân tích tài liệu thực tế. Tất cả các chỉ số trong bảng này đều là khoảng cách biên dịch; giá trị nhỏ hơn chứng tỏ hiệu suất tốt hơn. “Tokens” đại diện cho số lượng các ký hiệu được sử dụng trung bình trên mỗi trang; cụm “\(\mathrm{^{i + 200dpi}}\)” có nghĩa là sử dụng phương pháp Fitz để điều chỉnh độ phân giải hình ảnh gốc lên mức 200dpi. Đối với mô hình DeepSeek-OCR, các giá trị nằm trong ngoặc đơn ở cột “Tokens” là số lượng các ký hiệu hợp lệ được tính toán theo Phương trình 1.

**Bảng so sánh các mô hình nhận dạng văn bản**  

| **Mô hình**          | **Số lượng token được sử dụng** | **Điểm đánh giá tiếng Anh** | **Điểm đánh giá tiếng Trung** |
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

**Lưu ý:** Các chỉ số đánh giá được tính dựa trên nhiều yếu tố, bao gồm hiệu suất nhận diện văn bản, tốc độ xử lý, độ chính xác, v.v. Các con số trong bảng thể hiện thứ hạng của từng mô hình so với các mô hình khác trong cùng nhóm.

<|ref|>text<|/ref|><|det|>[[115, 727, 880, 775]]<|/det|>  
Nếu không sử dụng bố cục đặc biệt, có thể sử dụng dòng “<image>\nFree OCR.” để điều khiển định dạng đầu ra của mô hình. Tuy nhiên, định dạng đầu ra này vẫn chưa thể hoàn toàn tương thích với các tiêu chuẩn đánh giá của Fox; do đó, hiệu suất thực tế có thể cao hơn một chút so với kết quả đo lường.

<|ref|>text<|/ref|><|det|>[[115, 783, 881, 897]]<|/det|>
As shown in Table 2, within a \(10\times\) compression ratio, the model's decoding precision can reach approximately \(97\%\), which is a very promising result. In the future, it may be possible to achieve nearly \(10\times\) lossless contexts compression through text- to- image approaches. When the compression ratio exceeds \(10\times\), performance begins to decline, which may have two reasons: one is that the layout of long documents becomes more complex, and another reason may be that long texts become blurred at \(512\times 512\) or \(640\times 640\) resolution. The first issue can be solved by rendering texts onto a single layout page, while we believe the second issue will become<|ref|>text<|/ref|><|det|>[[115, 783, 881, 897]]<|/det|>  
Như được thể hiện trong Bảng 2, với tỷ lệ nén là 10 lần, độ chính xác khi giải mã dữ liệu bằng mô hình này có thể đạt khoảng 97%, đây là một kết quả rất đáng khích lệ. Trong tương lai, có thể sẽ có thể thực hiện được việc nén dữ liệu mà không làm mất thông tin với tỷ lệ gần 10 lần thông qua các phương pháp chuyển đổi văn bản thành hình ảnh. Tuy nhiên, khi tỷ lệ nén vượt quá 10 lần, hiệu suất của mô hình bắt đầu giảm sút; điều này có thể xuất phát từ hai lý do: thứ nhất là cấu trúc trang trình bày của các văn bản dài trở nên phức tạp hơn; thứ hai là các đoạn văn bản dài có thể bị mờ đi khi được hiển thị ở độ phân giải 512×512 hoặc 640×640. Vấn đề thứ nhất có thể được giải quyết bằng cách hiển thị toàn bộ nội dung văn bản trên cùng một trang, trong khi chúng tôi tin rằng vấn đề thứ hai cũng sẽ được khắc phục theo thời gian.

============================================================
--- Trang 12 ---
============================================================

<|ref|>text<|/ref|><|det|>[[115, 100, 881, 180]]<|/det|>
a feature of the forgetting mechanism. When compressing tokens by nearly \(20\times\), we find that precision can still approach \(60\%\). These results indicate that optical contexts compression is a very promising and worthwhile research direction, and this approach does not bring any overhead because it can leverage VLM infrastructure, as multimodal systems inherently require an additional vision encoder.<|ref|>text<|/ref|><|det|>[[115, 100, 881, 180]]<|/det|>  
Đây là một đặc điểm nổi bật của cơ chế quên lãng. Khi nén các dữ liệu này gần như \(20\times\), chúng ta vẫn có thể đạt được độ chính xác lên tới khoảng \(60\%\). Những kết quả này cho thấy rằng việc nén thông tin liên quan đến ngữ cảnh hình ảnh là một hướng nghiên cứu rất triển vọng và đáng giá; đồng thời, phương pháp này không gây ra bất kỳ gánh nặng nào vì nó có thể tận dụng trực tiếp cơ sở hạ tầng của các hệ thống VLM, trong khi các hệ thống đa phương thức vốn đã cần đến các bộ mã hóa hình ảnh bổ sung.

<|ref|>table_caption<|/ref|><|det|>[[115, 192, 881, 238]]<|/det|>
Bảng 4 | Khoảng cách cần thiết để chỉnh sửa các loại tài liệu khác nhau trong OmniDocBench. Kết quả cho thấy một số loại tài liệu có thể đạt được hiệu suất tốt chỉ với 64 hoặc 100 “token” hình ảnh, trong khi những loại khác lại yêu cầu phải sử dụng chế độ “Gundam”.

<|ref|>bảng</|/ref|><|det|>[[128, 250, 870, 380]]</|/det|>

<table><tr><td>Loại<br>Mức độ phân giải</td><td>Trang trình bày sách</td><td>Báo cáo tài chính</td><td>Sách giáo khoa</td><td>Bài thi</td><td>Tạp chí</td><>Luận văn học thuật</td><>Ghi chú</td><>Báo chí tổng thể</td></tr><tr><td>Cực nhỏ</td><td>0.147 0.116</td><td>0.207</td><td>0.173</td><td>0.294</td><td>0.201</td><td>0.395</td><td>0.297</td><td>0.94</td></tr><tr><td>Nhỏ</td><td>0.085 0.111</td><td>0.079</td><td>0.147</td><td>0.171</td><td>0.107</td><td>0.131</td><td>0.187</td><td>0.744</td></tr><tr><td>Trung bình</td><td>0.037 0.08</td><td>0.027</td><td>0.1</td><td>0.13</td><td>0.073</td><td>0.052</td><td>0.176</td><td>0.645</td></tr><tr><td>Lớn</td><td>0.038 0.108</td><td>0.022</td><td>0.084</td><td>0.109</td><td>0.06</td><td>0.053</td><td>0.155</td><td>0.353</td></tr><tr><td>Gundam</td><td>0.035 0.085</td><td>0.289</td><td>0.095</td><td>0.094</td><td>0.059</td><td>0.039</td><td>0.153</td><td>0.122</td></tr><tr><td>Guandam-M</td><td>0.052 0.09</td><td>0.034</td><td>0.091</td><td>0.079</td><td>0.079</td><td>0.048</td><td>0.1</td><td>0.099</td></tr></table>

<|ref|>title<|/ref|><|det|>[[115, 414, 385, 426]]<|/det|>
# 4.2. Hiệu suất thực tế của công nghệ OCR

<|ref|>text<|/ref|><|det|>[[115, 440, 883, 583]]<|/det|>  
DeepSeek-OCR không chỉ là một mô hình thử nghiệm mà còn sở hữu khả năng ứng dụng thực tế mạnh mẽ, đồng thời có thể được sử dụng để xây dựng dữ liệu phục vụ việc huấn luyện các mô hình LLM/VLM. Để đánh giá hiệu suất của DeepSeek-OCR, chúng tôi đã thử nghiệm nó trên bộ dữ liệu OmniDocBench [27]; kết quả được trình bày trong Bảng 3. Chỉ cần sử dụng 100 “token hình ảnh” (với độ phân giải 640x640), DeepSeek-OCR đã vượt trội hơn so với GOT-OCR2.0 [38] – mô hình yêu cầu sử dụng tới 256 token hình ảnh. Khi sử dụng 400 token hình ảnh (trong đó 285 token hữu ích, độ phân giải 1280x1280), DeepSeek-OCR đạt được hiệu suất ngang ngửa với các mô hình tiên tiến nhất trên bài kiểm thử này. Với lượng token hình ảnh ít hơn 800 (chế độ sử dụng “Gundam”), DeepSeek-OCR còn vượt trội hơn so với MinerU2.0 [34] – mô hình cần tới gần 7.000 token hình ảnh. Những kết quả này chứng minh rằng mô hình DeepSeek-OCR của chúng tôi rất mạnh mẽ trong các ứng dụng thực tế; đồng thời, nhờ khả năng nén dữ liệu hiệu quả, mô hình này còn tiềm năng phát triển cao hơn nữa trong lĩnh vực nghiên cứu khoa học.

<|ref|>text<|/ref|><|det|>[[115, 594, 883, 752]]<|/det|>  
Như được thể hiện trong Bảng 4, một số loại tài liệu chỉ cần rất ít các “token văn bản” là đã đạt được hiệu suất xử lý đáng mong đợi; ví dụ, các trang trình bày chỉ cần 64 “token văn bản” là đủ. Đối với các tài liệu sách hoặc báo cáo, phương pháp DeepSeek-OCR cũng có thể hoạt động hiệu quả với chỉ 100 “token văn bản”. Kết hợp với kết quả phân tích ở Phần 4.1, điều này có thể được giải thích do hầu hết các “token văn bản” trong những loại tài liệu này đều nằm trong khoảng từ 1.000 đến 5.000, nên tỷ lệ nén chúng không vượt quá 10 lần. Trong khi đó, đối với các tài liệu báo chí hoặc nội dung liên quan đến Gundam, cần sử dụng các chế độ nén chuyên biệt (như chế độ Gundam hay Gundam-Master) mới có thể đạt được độ chính xác xử lý đủ cao; bởi vì số lượng “token văn bản” trong những loại tài liệu này lên đến 4.000 đến 5.000, vượt xa mức 10 lần nén mà các chế độ khác có thể đạt được. Những kết quả thí nghiệm này càng làm rõ các giới hạn của phương pháp nén văn bản dựa trên ngữ cảnh, đồng thời cung cấp những thông tin hữu ích cho các nghiên cứu về việc tối ưu hóa cách thức xử lý “token văn bản” trong các hệ thống trí tuệ nhân tạo, cũng như các phương pháp nén dữ liệu dựa trên ngữ cảnh hoặc cơ chế “quên” thông tin trong các mô hình trí tuệ nhân tạo lớn.

<|ref|>title<|/ref|><|det|>[[115, 778, 306, 790]]<|/det|>
# 4.3. Nghiên cứu định tính

<|ref|>sub_title<|/ref|><|det|>[[115, 804, 278, 817]]<|/det|>
## 4.3.1. Phân tích sâu</td>

<|ref|>text<|/ref|><|det|>[[115, 830, 883, 891]]<|/det|>  
DeepSeek-OCR vừa sở hữu khả năng phân tích cấu trúc trang văn bản, vừa có thể thực hiện các thao tác nhận dạng ký tự quang học theo tiêu chuẩn OCR 2.0; điều này cho phép mô hình của chúng tôi tiếp tục phân tích các hình ảnh trong tài liệu thông qua việc gọi lại các mô hình phụ trợ, và chúng tôi gọi tính năng này là “phân tích sâu”. Như được minh họa trong Hình 7, 8, 9 và 10, mô hình của chúng tôi có thể thực hiện các thao tác phân tích sâu trên các biểu đồ, công thức hóa học, thậm chí cả các hình ảnh thông thường, và chỉ cần một yêu cầu đầu vào thống nhất là đủ.

============================================================
--- Trang 13 ---
============================================================

![Hình ảnh 0_0](images/page_13_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 810, 881, 875]]<|/thông tin chi tiết|>
<center>Hình 7 | Trong lĩnh vực báo cáo nghiên cứu tài chính, chế độ phân tích sâu của công cụ DeepSeek-OCR có thể được sử dụng để trích xuất các biểu đồ có cấu trúc rõ ràng từ các tài liệu. Biểu đồ là hình thức biểu diễn dữ liệu quan trọng trong lĩnh vực tài chính và khoa học; do đó, khả năng trích xuất thông tin từ các biểu đồ một cách có cấu trúc là yếu tố thiết yếu đối với các mô hình OCR trong tương lai.</center>

============================================================
--- Trang 14 ---
============================================================

![Hình ảnh 0_0](images/page_14_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin|>[[258, 465, 340, 477]]<|/thông tin|>
<center>Hình ảnh đầu vào</center>

![Hình ảnh 1_0](images/page_14_img_1_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[668, 460, 714, 472]]<|/thông tin chi tiết|>
<center>Kết quả</center>

![Hình 2_0](images/page_14_img_2_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 818, 881, 867]]<|/thông tin chi tiết|>
<center>Hình 8: Đối với sách và bài viết, chế độ phân tích sâu có thể tạo ra các chú thích chi tiết cho các hình ảnh trong tài liệu. Chỉ cần một yêu cầu nhỏ, mô hình có thể tự động xác định loại hình ảnh đó và hiển thị kết quả cần thiết.</center>

============================================================
--- Trang 15 ---
============================================================

![Hình ảnh 0_0](images/page_15_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[114, 817, 881, 866]]<|/thông tin chi tiết|>
<center>Hình 9: Chức năng nhận dạng văn bản bằng công nghệ OCR của DeepSeek-OCR, khi hoạt động ở chế độ phân tích sâu, cũng có thể nhận diện được các công thức hóa học trong các tài liệu khoa học và chuyển chúng sang định dạng SMILES. Trong tương lai, công nghệ OCR phiên bản 1.0 và 2.0 có thể đóng vai trò quan trọng trong sự phát triển của các mô hình trí tuệ nhân tạo dùng cho lĩnh vực Khoa học, Công nghệ, Kỹ thuật và Toán học.</center>

============================================================
--- Trang 16 ---
============================================================

![Hình ảnh 0_0](images/page_16_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 722, 881, 772]]<|/thông tin chi tiết|>
<center>Hình 10 | DeepSeek-OCR cũng có khả năng sao chép các hình dạng hình học đơn giản. Do mối quan hệ phức tạp giữa các đoạn thẳng trong các hình học này, việc phân tích chúng là một nhiệm vụ vô cùng thách thức và còn nhiều công việc phải làm trước khi đạt được kết quả mong muốn.</center>

<|ref|>title<|/ref|><|det|>[[117, 794, 371, 810]]<|/det|>
#### 4.3.2. Nhận dạng ngôn ngữ đa dạng

<|ref|>text<|/ref|><|det|>[[115, 820, 883, 902]]<|/det|>  
Các tài liệu PDF trên mạng Internet không chỉ chứa ngôn ngữ Trung Quốc và Anh, mà còn bao gồm rất nhiều dữ liệu đa ngôn ngữ; những dữ liệu này cũng đóng vai trò quan trọng trong quá trình huấn luyện các mô hình LLM. Đối với các tài liệu PDF, công cụ DeepSeek-OCR có thể xử lý gần 100 ngôn ngữ khác nhau. Giống như các tài liệu tiếng Trung và tiếng Anh, dữ liệu đa ngôn ngữ cũng được hỗ trợ trong cả các định dạng OCR có cấu trúc và không có cấu trúc. Kết quả đồ họa được trình bày trong Hình 11; chúng tôi đã chọn hai ngôn ngữ là tiếng Ả Rập và tiếng Sinhala để minh họa các kết quả này.

============================================================
--- Trang 17 ---
============================================================

![Hình ảnh 0_0](images/page_17_img_0_0.jpg)

<|ref|>image_caption<|/ref|><|det|>[[113, 789, 880, 839]]<|/det|>
<center>Hình 11: Để cho mô hình có khả năng xử lý các tệp PDF được thu thập từ nhiều nguồn khác nhau (dữ liệu đa ngôn ngữ), chúng tôi đã huấn luyện mô hình này với các công nghệ nhận dạng chữ viết quang học (OCR) dành cho gần 100 ngôn ngữ. Các tài liệu bằng ngôn ngữ thiểu số cũng có thể được xử lý thành cả dạng có cấu trúc trang trí và dạng không có cấu trúc trang trí, tùy thuộc vào các thông tin đầu vào được sử dụng.</center>

<|ref|>sub_title<|/ref|><|det|>[[113, 860, 415, 877]]<|/det|>
## 4.3.3. Hiểu biết tổng quát về hình ảnh

<|ref|>text<|/ref|><|det|>[[113, 888, 880, 920]]<|/det|>  
Chúng tôi cũng trang bị cho DeepSeek-OCR những khả năng nhất định trong việc hiểu biết về các hình ảnh nói chung. Kết quả minh họa liên quan được trình bày trong Hình 12.

============================================================
--- Trang 18 ---
============================================================

![Hình 0_0](images/page_18_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 660, 883, 743]]<|/thông tin chi tiết|>
<center>Hình 12: Mô hình DeepSeek-OCR vẫn giữ được các khả năng liên quan đến việc hiểu biết hình ảnh nói chung, bao gồm mô tả hình ảnh, phát hiện đối tượng, xác định vị trí đối tượng trong hình, v.v. Đồng thời, nhờ việc sử dụng dữ liệu chỉ chứa văn bản, khả năng xử lý ngôn ngữ của DeepSeek-OCR cũng được duy trì. Lưu ý rằng vì chúng tôi không áp dụng giai đoạn huấn luyện có giám sát (SFT), nên mô hình này không phải là một bot trò chuyện; một số chức năng chỉ có thể được kích hoạt khi có yêu cầu cụ thể từ người dùng.</center>

<|ref|>sub_title<|/ref|><|det|>[[117, 766, 255, 784]]<|/det|>
## 5. Thảo luận

<|ref|>text<|/ref|><|det|>[[115, 797, 883, 895]]<|/det|>  
Công trình nghiên cứu của chúng tôi đại diện cho những khám phá ban đầu về các giới hạn trong việc nén dữ liệu hình ảnh kết hợp văn bản; chúng tôi đã tìm hiểu xem cần bao nhiêu thông tin hình ảnh là đủ để giải mã một số lượng nhất định thông tin văn bản. Kết quả ban đầu rất đáng khích lệ: Phương pháp DeepSeek-OCR cho phép thực hiện việc nén dữ liệu gần như không mất thông tin, với tỷ lệ nén khoảng 10 lần; ngay cả khi tỷ lệ nén lên đến 20 lần, độ chính xác trong việc giải mã vẫn đạt mức 60%. Những phát hiện này mở ra những hướng đi hứa hẹn cho các ứng dụng tương lai, chẳng hạn như việc áp dụng các công nghệ xử lý hình ảnh trong các cuộc đối thoại có nhiều vòng, nhằm đạt được hiệu quả nén lên đến 10 lần.

============================================================
--- Trang 19 ---
============================================================

![Hình ảnh 0_0](images/page_19_img_0_0.jpg)
<|ref|>chú thích hình ảnh<|/ref|><|thông tin chi tiết|>[[115, 279, 883, 360]]<|/thông tin chi tiết|>
<center>Hình 13: Các cơ chế quên lãng là một trong những đặc điểm cơ bản nhất của trí nhớ con người. Phương pháp nén dữ liệu dựa trên nguyên lý này có thể mô phỏng cơ chế này bằng cách hiển thị các đoạn văn bản đã được sử dụng trước đó lên các hình ảnh để thực hiện việc nén ban đầu; sau đó, kích thước của các hình ảnh đó sẽ được điều chỉnh dần theo từng bước nhằm đạt được mức độ nén đa tầng. Trong quá trình này, số lượng các ký tự xuất hiện trong các hình ảnh sẽ giảm dần, và nội dung văn bản trên những hình ảnh đó cũng sẽ trở nên mờ nhạt hơn, qua đó thực hiện việc “quên lãng” thông tin đó.</center>

<|ref|>text<|/ref|><|det|>[[115, 384, 881, 499]]<|/det|>  
Đối với các trường hợp sử dụng trong quá khứ, chúng ta có thể dần dần giảm kích thước của các hình ảnh được hiển thị để tiếp tục giảm mức tiêu thụ tài nguyên. Giả định này lấy cảm hứng từ mối tương đồng tự nhiên giữa sự suy giảm khả năng ghi nhớ của con người theo thời gian và sự suy giảm khả năng nhận diện hình ảnh theo khoảng cách không gian – cả hai đều thể hiện những quy luật tương tự về việc mất dần thông tin theo thời gian, như được minh họa trong Hình 13. Bằng cách kết hợp các cơ chế này, phương pháp nén hình ảnh dựa trên nguyên lý này cho phép tạo ra một quá trình “mất dần thông tin” tương ứng với đường cong quên lãng sinh học: thông tin mới được lưu trữ với độ chính xác cao, trong khi thông tin cũ dần bị mất đi do tỷ lệ nén tăng lên.

<|ref|>text<|/ref|><|det|>[[115, 505, 882, 603]]<|/det|>  
Mặc dù những nghiên cứu ban đầu cho thấy tiềm năng trong việc xử lý các dữ liệu ngữ cảnh có quy mô lớn, trong đó các thông tin ngữ cảnh mới vẫn giữ được độ phân giải cao trong khi các thông tin ngữ cảnh cũ tiêu tốn ít tài nguyên hơn, chúng tôi cũng nhận thức rằng đây vẫn là những nghiên cứu ở giai đoạn sơ bộ và cần được tiếp tục khám phá thêm. Phương pháp này mở ra hướng đi để xây dựng các kiến trúc xử lý ngữ cảnh có khả năng xử lý lượng dữ liệu lớn một cách hiệu quả, đồng thời cân bằng giữa việc lưu trữ thông tin và các hạn chế về mặt tính toán; tuy nhiên, những ứng dụng thực tế và những hạn chế của các hệ thống nén dữ liệu loại này vẫn cần được nghiên cứu sâu hơn trong các công trình khoa học tương lai.

<|ref|>sub_title<|/ref|><|det|>[[115, 627, 258, 644]]<|/det|>
## 6. Kết luận

<|ref|>text<|/ref|><|det|>[[115, 657, 882, 820]]<|/det|>  
Trong báo cáo kỹ thuật này, chúng tôi đề xuất mô hình DeepSeek-OCR và đã kiểm chứng sơ bộ khả năng thực hiện việc nén thông tin văn bản dựa trên ngữ cảnh thông qua mô hình này. Kết quả cho thấy mô hình có thể giải mã các đoạn văn bản dài gấp hơn 10 lần so với số lượng dữ liệu hình ảnh được sử dụng để huấn luyện, chỉ từ một lượng dữ liệu nhỏ. Chúng tôi tin rằng phát hiện này sẽ góp phần thúc đẩy sự phát triển của các mô hình VLM và LLM trong tương lai. Ngoài ra, DeepSeek-OCR còn là một mô hình rất hữu ích, có khả năng tạo ra lượng lớn dữ liệu để huấn luyện mô hình trước khi chúng được sử dụng thực tế, từ đó trở thành công cụ hỗ trợ không thể thiếu cho các mô hình LLM. Tất nhiên, việc áp dụng công nghệ OCR một mình là chưa đủ để kiểm chứng đầy đủ tính hiệu quả của phương pháp nén thông tin văn bản dựa trên ngữ cảnh; chúng tôi sẽ tiếp tục tiến hành các bài kiểm tra bổ sung trong tương lai. Từ góc độ khác, lĩnh vực nén thông tin văn bản dựa trên ngữ cảnh vẫn còn nhiều tiềm năng để nghiên cứu và cải tiến, đây chính là một hướng đi đầy hứa hẹn cho tương lai.

============================================================
--- Trang 20 ---
============================================================

<|ref|>sub_title<|/ref|><|det|>[[115, 98, 227, 116]]<|/det|>
## Tài liệu tham khảo

<|ref|>text<|/ref|><|det|>[[117, 125, 884, 904]]<|/det|>
[1] Marker. Địa chỉ URL: https://github.com/datalab-to/marker. [2] Mathpix. Địa chỉ URL: https://mathpix.com/. [3] Ocrflux, 2025. Địa chỉ URL: https://github.com/chatdoc-com/OCRFlux. [4] G. AI. Gemini 2.5-pro, 2025. Địa chỉ URL: https://gemini.google.com/. [5] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, H. Zhong, Y. Zhu, M. Yang, Z. Li, J. Wan, P. Wang, W. Ding, Z. Fu, Y. Xu, J. Ye, X. Zhang, T. Xie, Z. Cheng, H. Zhang, Z. Yang, H. Xu và J. Lin. Báo cáo kỹ thuật về Qwen2.5-vl. Bản thảo trên arXiv: arXiv:2502.13923, 2025. [6] L. Blecher, G. Cucurull, T. Scialom và R. Stojnic. Nougat: Công cụ hỗ trợ việc phân tích nội dung các tài liệu học thuật thông qua công nghệ thị giác nhân tạo. Bản thảo trên arXiv: arXiv:2308.13418, 2023. [7] J. Chen, L. Kong, H. Wei, C. Liu, Z. Ge, L. Zhao, J. Sun, C. Han và X. Zhang. Onechart: Phương pháp trích xuất thông tin từ biểu đồ thông qua một ký hiệu hỗ trợ đặc biệt. Trong ấn phẩm của Hội nghị Quốc tế về Đa phương tiện truyền thông lần thứ 32 của ACM, trang 147–155, 2024. [8] Z. Chen, W. Wang, H. Tian, S. Ye, Z. Gao, E. Cui, W. Tong, K. Hu, J. Luo, Z. Ma và cộng sự. Chúng ta còn cách bằng mấy so với mô hình GPT-4v? Cách nào để thu hẹp khoảng cách với các mô hình đa phương tiện thương mại sử dụng các bộ công cụ mã nguồn mở? Bản thảo trên arXiv: arXiv:2404.16821, 2024. [9] C. Cui, T. Sun, M. Lin, T. Gao, Y. Zhang, J. Liu, X. Wang, Z. Zhang, C. Zhou, H. Liu và cộng sự. Báo cáo kỹ thuật về Paddleocr 3.0. Bản thảo trên arXiv: arXiv:2507.05595, 2025. [10] M. Dehghani, J. Djolonga, B. Mustafa, P. Padlewski, J. Heek, J. Gilmer, A. Steiner, M. Caron, R. Geirhos, I. Alabdulmohsin và cộng sự. Patch n’ Pack: Navit – một công cụ xử lý hình ảnh linh hoạt, phù hợp với mọi tỷ lệ khung hình và độ phân giải. Tạp chí Advances in Neural Information Processing Systems, tập 36, trang 3632–3656, 2023. [11] H. Feng, S. Wei, X. Fei, W. Shi, Y. Han, L. Liao, J. Lu, B. Wu, Q. Liu, C. Lin và cộng sự. Dolphin: Phương pháp phân tích hình ảnh tài liệu thông qua các gợi ý đa dạng. Bản thảo trên arXiv: arXiv:2505.14059, 2025. [12] Y. Goyal, T. Khot, D. Summers-Stay, D. Batra và D. Parikh. Tăng tầm quan trọng của khả năng hiểu hình ảnh trong việc trả lời câu hỏi hình ảnh. Trong Tài liệu hội nghị IEEE về thị giác máy tính và nhận diện mẫu, trang 6904–6913, 2017. [13] J. Gu, X. Meng, G. Lu, L. Hou, N. Minzhe, X. Liang, L. Yao, R. Huang, W. Zhang, X. Jiang và cộng sự. Wukong: Mô hình huấn luyện đa模态 quy mô lớn, sử dụng dữ liệu tiếng Trung, được phát triển bởi 100 triệu dữ liệu. Tạp chí Advances in Neural Information Processing Systems, 35:26418–26431, 2022. [14] High- flyer. HAI-LLM: Công cụ huấn luyện hiệu quả và nhẹ nhàng cho các mô hình lớn, 2023. Địa chỉ web: https://www.high- flyers.cn/en/blog/hai-llm. [15] S. Iyer, X. V. Lin, R. Pasunuru, T. Mihaylov, D. Simig, P. Yu, K. Shuster, T. Wang, Q. Liu, P. S. Koura và cộng sự. Opt-Iml: Phương pháp học máy để tối ưu hóa quá trình huấn luyện các mô hình ngôn ngữ, dựa trên khả năng tổng quát hóa. Bản thảo trên arXiv: arXiv:2212.12017, 2022. [16] S. Kazemzadeh, V. Ordonez, M. Matten và T. Berg. Referitgame: Công cụ nhận diện đối tượng trong các hình ảnh về cảnh thiên nhiên. Trong Tài liệu hội nghị EMNLP năm 2014 về các phương pháp thực nghiệm trong xử lý ngôn ngữ tự nhiên, trang 787–798, 2014.

============================================================
--- Trang 21 ---
============================================================

<|ref|>text<|/ref|><|det|>[[113, 100, 885, 135]]<|/det|>  
[17] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.-Y. Lo và cộng sự. “Việc phân đoạn bất cứ thứ gì đều trở nên khả thi.” Bản thảo trên arXiv: arXiv:2304.02643, 2023.

<|ref|>text<|/ref|><|det|>[[115, 143, 884, 192]]<|/det|>  
[18] Z. Li, Y. Liu, Q. Liu, Z. Ma, Z. Zhang, S. Zhang, Z. Guo, J. Zhang, X. Wang và X. Bai. Monkeyocr: Phương pháp phân tích văn bản dựa trên mô hình ba yếu tố – cấu trúc, mối quan hệ giữa các thành phần trong văn bản. Bản thảo nghiên cứu trên arXiv: arXiv:2506.05218, 2025.

<|ref|>text<|/ref|><|det|>[[115, 201, 884, 251]]<|/det|>  
[19] A. Liu, B. Feng, B. Wang, B. Wang, B. Liu, C. Zhao, C. Deng, C. Ruan, D. Dai, D. Guo và cộng sự. Deepseek-v2: Một mô hình ngôn ngữ dựa trên kết hợp ý kiến của nhiều chuyên gia, vừa mạnh mẽ, vừa tiết kiệm tài nguyên và hiệu quả trong việc xử lý dữ liệu. Bản thảo gốc trên arXiv: arXiv:2405.04434, 2024.

<|ref|>text<|/ref|><|det|>[[115, 260, 884, 294]]<|/det|>  
[20] A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan và cộng sự. Báo cáo kỹ thuật về Deepseek-v3. Bản thảo trên arXiv: arXiv:2412.19437, 2024.

<|ref|>text<|/ref|><|det|>[[115, 303, 884, 353]]<|/det|>  
[21] C. Liu, H. Wei, J. Chen, L. Kong, Z. Ge, Z. Zhu, L. Zhao, J. Sun, C. Han và X. Zhang. Khả năng hiểu nội dung các tài liệu gồm nhiều trang một cách chi tiết, bất kể vị trí nào được chọn làm điểm tập trung. Bản thảo trên arXiv: arXiv:2405.14295, 2024.

<|ref|>text<|/ref|><|det|>[[115, 362, 881, 395]]<|/det|>
[22] I. Loshchilov và F. Hutter. Phương pháp hạ dốc gradient ngẫu nhiên với cơ chế khởi động lại. Bản thảo trên arXiv: arXiv:1608.03983, 2016.

<|ref|>text<|/ref|><|det|>[[115, 404, 830, 422]]<|/det|>
[23] I. Loshchilov và F. Hutter. Phương pháp điều chỉnh độ suy giảm trọng số không phụ thuộc lẫn nhau. Trong hội nghị ICLR, 2019.

<|ref|>text<|/ref|><|det|>[[115, 431, 884, 481]]<|/det|>  
[24] A. Masry, D. X. Long, J. Q. Tan, S. Joty và E. Hoque. Chartqa: Một công cụ đánh giá hiệu suất các hệ thống trả lời câu hỏi liên quan đến biểu đồ, với khả năng suy luận vừa dựa trên thông tin trực quan vừa dựa trên lô-gic. Bản thảo nghiên cứu trên arXiv: arXiv:2203.10244, 2022.

<|ref|>text<|/ref|><|det|>[[115, 490, 884, 555]]<|/det|>  
[25] A. Nassar, A. Marafioti, M. Omenetti, M. Lysak, N. Livathinos, C. Auer, L. Morin, R. T. de Lima, Y. Kim, A. S. Gurbuz và cộng sự. Smoldocling: Một mô hình học máy siêu nhỏ gọn dành cho việc chuyển đổi tài liệu đa phương thức một cách tự động. Bản thảo trên arXiv: arXiv:2503.11576, 2025.

<|ref|>text<|/ref|><|det|>[[115, 565, 461, 583]]<|/det|>
[26] OpenAI. Báo cáo kỹ thuật về GPT-4, 2023.

<|ref|>text<|/ref|><|det|>[[115, 592, 884, 658]]<|/det|>
[27] L. Ouyang, Y. Qu, H. Zhou, J. Zhu, R. Zhang, Q. Lin, B. Wang, Z. Zhao, M. Jiang, X. Zhao và cộng sự. Omnidocbench: Công cụ đánh giá hiệu suất các phương pháp xử lý tài liệu PDF với các bình luận chi tiết. Trong Tài liệu hội nghị Thị giác máy tính và Nhận dạng mẫu, trang 24838–24848, năm 2025.

<|ref|>text<|/ref|><|det|>[[115, 667, 884, 716]]<|/det|>  
[28] J. Poznanski, A. Rangapur, J. Borchardt, J. Dunkelberger, R. Huff, D. Lin, C. Wilhelm, K. Lo và L. Soldaini. olmocr: Giải mã hàng nghìn tỷ token trong các tệp PDF bằng các mô hình ngôn ngữ hình ảnh. Bản thảo trên arXiv: arXiv:2502.18443, 2025.

<|ref|>text<|/ref|><|det|>[[115, 726, 884, 791]]<|/det|>  
[29] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark và cộng sự. Việc xây dựng các mô hình thị giác có khả năng được áp dụng rộng rãi thông qua việc học từ dữ liệu ngôn ngữ tự nhiên. Trong Hội nghị Quốc tế về Máy học, trang 8748–8763. PMLR, 2021.

<|ref|>text<|/ref|><|det|>[[115, 801, 839, 819]]<|/det|>  
[30] Rednote. dots.ocr, 2025. Địa chỉ URL: https://github.com/rednote-hilab/dots.ocr.

<|ref|>text<|/ref|><|det|>[[115, 828, 884, 877]]<|/det|>  
[31] C. Schuhmann, R. Vencu, R. Beaumont, R. Kaczmarczyk, C. Mullis, A. Katta, T. Coombes, J. Jitsev và A. Komatsuzaki. Laion-400m: Bộ dữ liệu mở chứa 400 triệu cặp hình ảnh kèm văn bản đã được lọc. Bản thảo trên arXiv: arXiv:2111.02114, 2021.

============================================================
--- Trang 22 ---
============================================================

<|ref|>text<|/ref|><|det|>[[113, 99, 885, 151]]<|/det|>  
[32] A. Singh, V. Natarajan, M. Shah, Y. Jiang, X. Chen, D. Batra, D. Parikh và M. Rohrbach. Những nỗ lực nhằm phát triển các mô hình nhận diện hình ảnh có khả năng “đọc” thông tin. Trong tài liệu báo cáo hội nghị IEEE/CVF về thị giác máy tính và nhận dạng mẫu, trang 8317–8326, năm 2019.

<|ref|>text<|/ref|><|det|>[[113, 157, 884, 192]]<|/det|>  
[33] T. Sun, C. Cui, Y. Du và Y. Liu. Pp-dcolayout: Một mô hình thống nhất để phát hiện cách bố trí nội dung tài liệu, nhằm tăng tốc độ xử lý dữ liệu quy mô lớn. Bản thảo trên arXiv: arXiv:2503.17213, 2025.

<|ref|>text<|/ref|><|det|>[[114, 201, 884, 251]]<|/det|>  
[34] B. Wang, C. Xu, X. Zhao, L. Ouyang, F. Wu, Z. Zhao, R. Xu, K. Liu, Y. Qu, F. Shang, v.v. Mineru: Một giải pháp mã nguồn mở dùng để trích xuất nội dung tài liệu một cách chính xác. Bản thảo trên arXiv: arXiv:2409.18839, 2024.

<|ref|>text<|/ref|><|det|>[[114, 260, 884, 310]]<|/det|>
[35] P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge và cộng sự. Qwen2-vl: Nâng cao khả năng nhận thức thế giới của các mô hình học máy ngôn ngữ-viễn thị ở mọi độ phân giải. Bản thảo trên arXiv: arXiv:2409.12191, 2024.

<|ref|>text<|/ref|><|det|>[[114, 319, 884, 370]]<|/det|>
[36] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, J. Yang, J. Sun, C. Han và X. Zhang. Vary: Phương pháp mở rộng vốn từ ngữ liên quan đến hình ảnh dành cho các mô hình ngôn ngữ-viễn thị quy mô lớn. Trong Hội nghị Châu Âu về Thị giác Máy tính, trang 408–424. Springer, 2024.

<|ref|>text<|/ref|><|det|>[[114, 378, 884, 428]]<|/det|>  
[37] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, E. Yu, J. Sun, C. Han và X. Zhang. Mô hình ngôn ngữ nhỏ kết hợp với bộ từ vựng hỗ trợ thị giác. Bản thảo trên arXiv: arXiv:2401.12503, 2024.

<|ref|>text<|/ref|><|det|>[[114, 436, 884, 487]]<|/det|>  
[38] H. Wei, C. Liu, J. Chen, J. Wang, L. Kong, Y. Xu, Z. Ge, L. Zhao, J. Sun, Y. Peng và cộng sự. Lý thuyết chung về công nghệ nhận dạng ký tự quang học: Hướng tới phiên bản OCR 2.0 thông qua một mô hình tích hợp từ đầu đến cuối. Bản thảo trên arXiv: arXiv:2409.01704, 2024.

<|ref|>text<|/ref|><|det|>[[113, 495, 884, 530]]<|/det|>  
[39] H. Wei, Y. Yin, Y. Li, J. Wang, L. Zhao, J. Sun, Z. Ge, X. Zhang và D. Jiang. Nhận thức chậm rãi: Hãy cùng nhận diện các hình học một cách từng bước một. Bản thảo trên arXiv: arXiv:2412.20631, 2024.

<|ref|>text<|/ref|><|det|>[[114, 538, 884, 589]]<|/det|>
[40] Z. Wu, X. Chen, Z. Pan, X. Liu, W. Liu, D. Dai, H. Gao, Y. Ma, C. Wu, B. Wang và cộng sự. Deepseek-vl2: Các mô hình học máy thị giác-ngôn ngữ dựa trên kết hợp kiến thức của nhiều chuyên gia, nhằm nâng cao khả năng hiểu biết đa phương thức. Bản thảo trước khi công bố trên arXiv: arXiv:2412.10302, 2024.

<|ref|>text<|/ref|><|det|>[[113, 597, 884, 632]]<|/det|>  
[41] W. Yu, Z. Yang, L. Li, J. Wang, K. Lin, Z. Liu, X. Wang và L. Wang. Mm-Vet: Đánh giá các mô hình đa phương thức lớn về khả năng tích hợp đa chức năng. Bản thảo trên arXiv: arXiv:2308.02490, 2023.

<|ref|>text<|/ref|><|det|>[[114, 640, 884, 690]]<|/det|>
[42] J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao và cộng sự. Internvl3: Nghiên cứu các phương pháp huấn luyện và đánh giá tiên tiến cho các mô hình đa模态 mã nguồn mở. Bản thảo trên arXiv: arXiv:2504.10479, 2025.