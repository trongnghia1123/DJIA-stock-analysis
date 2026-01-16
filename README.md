# 📊 Phân tích cổ phiếu DJIA – Dự án phân tích dữ liệu đầu tư

## 📌 Giới thiệu

Dự án này tập trung vào **phân tích dữ liệu giá cổ phiếu và thông tin doanh nghiệp trong bộ chỉ số Dow Jones Industrial Average (DJIA)** nhằm trả lời câu hỏi:

> **Nếu là một nhà đầu tư, nên lựa chọn ngành nghề và doanh nghiệp nào để đầu tư dựa trên dữ liệu?**

Dự án bao phủ toàn bộ quy trình xử lý dữ liệu:

* Thu thập dữ liệu
* Làm sạch & kiểm tra dữ liệu
* Lưu trữ dữ liệu trong PostgreSQL
* Phân tích dữ liệu khám phá (EDA)
* Trực quan hóa và rút ra insight

---

## 🧠 Mục tiêu phân tích

* So sánh các **ngành (sector)** theo:

  * Tổng khối lượng giao dịch
  * Tổng vốn hóa thị trường
  * Giá đóng cửa trung bình
* Phân tích **xu hướng giá theo thời gian** của các ngành
* So sánh các **doanh nghiệp trong cùng ngành**
* Kết hợp dữ liệu giá và dữ liệu doanh nghiệp để đưa ra góc nhìn đầu tư

---

## 🗂 Dữ liệu sử dụng

### 1️⃣ Dữ liệu giá cổ phiếu

* Dữ liệu OHLCV theo ngày
* Thời gian: **Jan/2023 – Jan/2026**
* Các trường chính:

  * `date, open, high, low, close, volume, ticker`

### 2️⃣ Dữ liệu thông tin doanh nghiệp

* Thông tin mô tả và chỉ số cơ bản:

  * `symbol, name, sector, industry`
  * `market_cap, pe_ratio, dividend_yield`
  * `52_week_high, 52_week_low`

📌 **Nguồn dữ liệu**: Yahoo Finance (qua thư viện `yfinance`)

---

## 🏗️ Kiến trúc dữ liệu

```text
Yahoo Finance
     ↓
   CSV
     ↓
 PostgreSQL
   ├── dim_company (thông tin doanh nghiệp)
   └── fact_stock_price (giá cổ phiếu theo ngày)
     ↓
 Pandas DataFrame
     ↓
 Phân tích & Trực quan hóa
```

### Thiết kế database

* **Primary key**

  * `dim_company.symbol`
* **Foreign key**

  * `fact_stock_price.ticker → dim_company.symbol`

Thiết kế theo mô hình **fact – dimension** giúp thuận tiện cho phân tích.

---

## 🛠 Công nghệ sử dụng

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* PostgreSQL
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub

---

## 📊 Nội dung phân tích chính

* Kiểm tra chất lượng dữ liệu (missing values, kiểu dữ liệu)
* Phân bố ngành trong bộ DJIA
* Tổng khối lượng giao dịch theo ngành (biểu đồ cột)
* Tổng vốn hóa theo ngành (biểu đồ cột)
* Giá đóng cửa trung bình theo ngành và theo thời gian (biểu đồ đường)
* Phân tích top 5 ngành nổi bật
* So sánh doanh nghiệp trong từng ngành
* Nhận diện xu hướng và đặc điểm đầu tư của từng nhóm ngành

---

## 💡 Insight tiêu biểu

* Ngành **Technology** chiếm tỷ trọng lớn nhất về số lượng công ty và vốn hóa.
* Ngành **Financial Services** có mức giá đóng cửa trung bình cao dù số lượng công ty ít hơn.
* Ngành có khối lượng giao dịch lớn thường có tính thanh khoản cao.
* Một số doanh nghiệp giao dịch gần vùng giá thấp của 52 tuần, có thể là điểm quan sát đáng chú ý.

---

## 📁 Cấu trúc thư mục

```text
djia-stock-analysis/
│
├── data/
│   ├── djia_stock_price.csv
│   ├── djia_company_info.csv
│   ├── get_stock_price.py
│   ├── get_companies_info.py
│   └── check_data.py
│
├── sql/
│   ├── pipeline_stock_price.py
│   └── pipeline_companies_info.py
│
├── Analyst.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Cách chạy dự án

### 1️⃣ Cài thư viện

```bash
pip install -r requirements.txt
```

### 2️⃣ Thu thập dữ liệu

```bash
python data/get_stock_price.py
python data/get_companies_info.py
```

### 3️⃣ Load dữ liệu vào PostgreSQL

```bash
python sql/pipeline_companies_info.py
python sql/pipeline_stock_price.py
```

### 4️⃣ Phân tích dữ liệu

```bash
jupyter notebook Analyst.ipynb
```

---

## 🚀 Hướng phát triển tiếp theo

* Bổ sung chỉ báo kỹ thuật (Moving Average, RSI)
* Phân tích rủi ro & biến động giá
* Trực quan hóa bằng dashboard (Power BI / Tableau)
* Mở rộng sang các chỉ số khác như S&P 500

```bash 
* Tại vì hơi lười nên mình có dùng AI để viết một vài chỗ trong README nhé :)) *
```
