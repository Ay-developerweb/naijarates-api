# NaijaRates API

> A free, open-source REST API for real-time Nigerian exchange rates, fuel prices, and commodity market data.

Nigeria runs on data that's hard to access programmatically. Bank rates differ from street rates. Fuel prices shift weekly. Market data is scattered across PDFs, news sites, and WhatsApp groups. NaijaRates API fixes that — one clean API, consistently updated, free to use.

---

## What It Does

- Returns current USD/NGN, GBP/NGN, EUR/NGN exchange rates (official CBN rate + parallel market rate)
- Tracks current fuel pump prices across Nigerian states
- Exposes commodity price data (rice, cement, diesel) updated on a schedule
- Lightweight, fast, and built to be embedded in apps, bots, dashboards, and scripts

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11+ |
| Scheduler | APScheduler |
| Data Storage | SQLite (dev) / PostgreSQL (prod) |
| Containerization | Docker + Docker Compose |
| Docs | Auto-generated via Swagger UI |

---

## Project Structure

```
naijarates-api/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── routes/
│   │   ├── exchange.py      # Exchange rate endpoints
│   │   ├── fuel.py          # Fuel price endpoints
│   │   └── commodities.py   # Commodity price endpoints
│   ├── scheduler/
│   │   └── jobs.py          # APScheduler data refresh jobs
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   └── db/
│       └── database.py      # DB connection and setup
├── tests/
│   └── test_routes.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Exchange Rates

```
GET /rates/exchange
```

Returns current exchange rates from both CBN official and parallel market sources.

**Sample Response:**
```json
{
  "timestamp": "2026-03-31T10:00:00Z",
  "base_currency": "NGN",
  "rates": {
    "USD": {
      "cbn_official": 1580.50,
      "parallel_market": 1615.00
    },
    "GBP": {
      "cbn_official": 2010.30,
      "parallel_market": 2045.00
    },
    "EUR": {
      "cbn_official": 1720.00,
      "parallel_market": 1755.00
    }
  }
}
```

---

### Fuel Prices

```
GET /rates/fuel
```

Returns current pump prices per litre across Nigeria.

**Sample Response:**
```json
{
  "timestamp": "2026-03-31T10:00:00Z",
  "currency": "NGN",
  "prices_per_litre": {
    "PMS": 897.00,
    "diesel": 1210.00,
    "kerosene": 1450.00
  },
  "note": "Prices reflect national average. Regional variation may apply."
}
```

---

### Commodities

```
GET /rates/commodities
```

Returns current market prices for key Nigerian commodities.

**Sample Response:**
```json
{
  "timestamp": "2026-03-31T10:00:00Z",
  "currency": "NGN",
  "commodities": {
    "rice_50kg_bag": 85000,
    "cement_50kg_bag": 9500,
    "cooking_gas_per_kg": 1800
  }
}
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker (optional but recommended)

### Run Locally

```bash
# Clone the repo
git clone https://github.com/aython-dev/naijarates-api.git
cd naijarates-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Run with Docker

```bash
docker-compose up --build
```

---

## Scheduler

Data is refreshed automatically using APScheduler:

| Data Type | Refresh Interval |
|---|---|
| Exchange rates | Every 6 hours |
| Fuel prices | Every 24 hours |
| Commodities | Every 48 hours |

---

## Roadmap

- [x] Project structure and API design
- [ ] Exchange rate scraper and scheduler
- [ ] Fuel price data integration
- [ ] Commodity price endpoint
- [ ] Docker setup
- [ ] PostgreSQL production config
- [ ] Rate limiting and API key support
- [ ] Public deployment (Railway / Render)
- [ ] Historical data endpoint

---

## Why I Built This

Nigerian developers building fintech apps, budget tools, e-commerce platforms, or just weekend projects constantly hit the same wall: there's no clean, free, programmatic way to get basic economic data for Nigeria.

This project exists to change that, starting small and building toward something the ecosystem can actually rely on.

---

## Contributing

Contributions are welcome. If you know a reliable data source for any of the endpoints above, open an issue or submit a PR.

---

## License

MIT License. Free to use, fork, and build on.

---

## Author

**Ayomide Adediran**
Backend Engineer | Python, FastAPI, Rust
Ibadan, Nigeria

[Portfolio](https://aython-site.vercel.app) | [Email](mailto:ayomideadediran45@gmail.com) | [WhatsApp](https://wa.me/2349074140454)