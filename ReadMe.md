# NaijaRates API

> A professional-grade, open-source REST API for real-time Nigerian exchange rates, fuel prices, and commodity market data.

NaijaRates API provides a structured, programmatic way to access critical Nigerian economic data. Built with FastAPI and powered by background scrapers, it ensures that developers have access to consistent, up-to-date indicators for their applications.

---

## 🚀 Features

- **Multi-Source Exchange Rates**: USD/NGN, GBP/NGN, and EUR/NGN (Official CBN vs. Parallel Market).
- **National Fuel Prices**: Track national average pump prices for PMS, Diesel, and Kerosene.
- **Commodity Market Tracking**: Key market prices for essential goods like Rice and Cement.
- **Professional Architecture**: Clean Service Layer, Background Schedulers, and Persistent Storage.
- **Enterprise-Ready**: Dockerized, versioned API, and fully documented with Swagger/OpenAPI.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11+ |
| Scheduler | APScheduler |
| Config | Pydantic Settings & Dotenv |
| Data Storage | SQLite (Local/Dev) / PostgreSQL compatible |
| Containerization | Docker + Docker Compose |
| Documentation | Swagger UI & ReDoc |

---

## 📁 Project Structure

```text
naijarates-api/
├── app/
│   ├── core/
│   │   └── config.py        # Centralized settings & env management
│   ├── services/
│   │   ├── data_service.py  # Data extraction & business logic
│   │   └── scraper.py       # Market scraping & ingestion engine
│   ├── routes/
│   │   ├── exchange.py      # Exchange rate controllers
│   │   ├── fuel.py          # Fuel price controllers
│   │   └── commodities.py   # Commodity price controllers
│   ├── scheduler/
│   │   └── jobs.py          # Background refresh job definitions
│   ├── models/
│   │   └── schemas.py       # Pydantic validation & documentation schemas
│   ├── db/
│   │   └── database.py      # SQLAlchemy connection & models
│   └── main.py              # Application entry point & middleware
├── tests/
│   └── test_routes.py       # API integrity tests
├── Dockerfile               # Production-ready image
├── docker-compose.yml       # Orchestration
├── requirements.txt         # Dependency manifest
└── README.md
```

---

## 📡 API Documentation

Visit `{host}/docs` for the interactive Swagger UI or `{host}/redoc` for detailed API documentation.

### Base URL: `http://localhost:8000/api/v1`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/rates/exchange` | USD, GBP, EUR (CBN/Parallel) |
| `GET` | `/rates/fuel` | PMS, Diesel, Kerosene prices |
| `GET` | `/rates/commodities` | Rice, Cement, Cooking Gas |
| `GET` | `/` | System health & version status |

---

## 🏁 Getting Started

### Run Locally

1. **Clone & Enter Directory:**
   ```bash
   git clone https://github.com/Ay-developerweb/naijarates-api.git
   cd naijarates-api
   ```

2. **Setup Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   copy .env.example .env     # Windows: copy .env.example .env
   ```

3. **Start the Engine:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Run with Docker

```bash
docker-compose up --build
```

---

## 🔄 Data Refresh Schedule

The system automatically updates its internal database using background workers:

| Category | Frequency |
|---|---|
| **Exchange Rates** | Every 6 Hours |
| **Fuel Prices** | Every 24 Hours |
| **Commodities** | Every 48 Hours |

---

## 🗺️ Roadmap

- [x] Versioned API Design (`/v1`)
- [x] Professional Service/Scraper Layer
- [x] Background Ingestion Engine
- [x] Persistence Layer (SQLite/JSON)
- [x] Dockerization
- [ ] Implement live BeautifulSoup scrapers for specific sites
- [ ] PostgreSQL production configuration
- [ ] API Key & Rate Limiting
- [ ] Historical Data Time-series endpoints

---

## ✍️ Author

**Ayomide Adediran**
Backend Engineer | Python, FastAPI, Rust
[Portfolio](https://aython-site.vercel.app) | [WhatsApp](https://wa.me/2349074140454)

---

## 📜 License

MIT License. Free to use, fork, and build on.
