```markdown
# 📦 Data Preparation API

**Version:** 1.0.0  
**Author:** Aerhed AI

---

## 📝 Overview

The **Data Preparation API** is a modular microservice for preparing datasets for downstream machine learning tasks.  
It is built using the [Aerhed AI Python API Template](https://github.com/aerhedai/python-api-template) and includes:

- **Scaling**: MinMaxScaler, StandardScaler, RobustScaler, etc.
- **Encoding**: One-hot encoding, label encoding for categorical variables.
- **Splitting**: Train-test split (with optional stratification).
- **Output**: Saves processed dataset and metadata for further processing.

This API is designed to integrate seamlessly with other Aerhed modular APIs in the AI dataset pipeline.

---

## 📂 Project Structure

```
data-preparation-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   └── prepare.py           # API route definitions
│   ├── services/
│   │   ├── __init__.py
│   │   └── preparation_service.py  # Core preparation logic
│   ├── models/
│   │   ├── __init__.py
│   │   └── preparation_request.py  # Pydantic models for requests
│   ├── utils/
│   │   ├── __init__.py
│   │   └── file_handler.py      # File loading/saving helpers
├── tests/
│   ├── __init__.py
│   └── test_preparation.py      # Unit tests
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
└── start.sh
```

---

## 🚀 Features

- 📤 **Upload** dataset in CSV/Excel format (via shared volume or API call).
- 🛠 **Clean & transform**:
  - Encode categorical features
  - Scale numerical features
  - Handle missing values
- ✂ **Split** into training/testing sets
- 📦 **Save outputs** for downstream APIs

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/aerhedai/data-preparation-api.git
cd data-preparation-api
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Copy `.env.example` to `.env` and update values if necessary:

```bash
cp .env.example .env
```

Example `.env`:

```
HOST=0.0.0.0
PORT=8000
UPLOAD_DIR=uploaded_files
OUTPUT_DIR=prepared_files
```

---

## ▶️ Running the API

### Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docker
```bash
docker build -t data-preparation-api .
docker run -p 8000:8000 data-preparation-api
```

### Docker Compose
If integrating with other APIs:
```bash
docker-compose up --build
```

---

## 📡 API Endpoints

### **POST** `/prepare`
Prepares a dataset for ML.

**Request:**
```json
{
  "file_path": "uploaded_files/my_dataset.csv",
  "target_column": "price",
  "scaling": "standard",
  "encoding": "onehot",
  "test_size": 0.2,
  "stratify": true
}
```

**Response:**
```json
{
  "train_file": "prepared_files/train.csv",
  "test_file": "prepared_files/test.csv",
  "scaler": "StandardScaler",
  "encoder": "OneHotEncoder"
}
```

---

## 🧪 Testing

Run unit tests with:

```bash
pytest
```

---

## 🛠 Development Notes

- **Preparation logic** lives in `app/services/preparation_service.py`
- **Request validation** in `app/models/preparation_request.py`
- **File handling** in `app/utils/file_handler.py`
- **Routes** in `app/routes/prepare.py`

---

## 🔗 Related APIs

- [`dataset-uploader-api`](https://github.com/aerhedai/dataset-uploader-api)
- [`data-profiler-api`](https://github.com/aerhedai/data-profiler-api)
- [`data-cleaner-api`](https://github.com/aerhedai/data-cleaner-api)

---

## 📜 License
MIT License – see [LICENSE](LICENSE) for details.
```
