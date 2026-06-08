# 🐦 Turkey Bird Atlas — SQL Project

**Course:** Applied SQL — Uygulamalı SQL  
**Student:** Arda Taştan | 24025019 | Department of Mathematics, Yıldız Technical University  

---

## About

A relational SQLite database integrated with a Python Flask web application. It stores and organizes data about bird species found in Turkey. The database includes species names (Turkish & Latin), IUCN conservation status, habitat types, and regional distribution. It also features a dynamic observation logging system where users can record field sightings that are instantly linked to the main species database.

---

## Database Schema

2 main tables connected by a foreign key relationship with the following column structures:

### 1. `species` Table (Main Catalog)
Stores static taxonomic and geographical data for 513 bird species.

| Column Name | Data Type | Description |
|---|---|---|
| `id` | INTEGER | Primary Key (Auto-incremented) |
| `name_tr` | TEXT | Turkish common name of the bird species (Not Null) |
| `name_latin` | TEXT | Scientific Latin name |
| `habitat_name`| TEXT | Primary habitat type (e.g., wetland, forest, steppe) |
| `region_name` | TEXT | Geographic region distribution in Turkey |
| `conservation_status` | TEXT | IUCN Red List threat category (e.g., LC, VU, EN) |

### 2. `observations` Table (User Field Sightings)
Stores dynamic field notes submitted by users, linked directly to the species catalog.

| Column Name | Data Type | Description |
|---|---|---|
| `id` | INTEGER | Primary Key (Auto-incremented) |
| `bird_id` | INTEGER | Foreign Key (References `species.id`) |
| `note` | TEXT | User's specific field notes or observations |

---

## SQL Features Used

- `JOIN` (INNER) — Combines the observation records with the species table to fetch dynamic Turkish names instead of raw IDs.
- `PRIMARY KEY` & `AUTOINCREMENT` — Ensures each species and observation has a unique, automatically incrementing identifier.
- `FOREIGN KEY` — Establishes a strict relationship by linking `bird_id` in the observations table to the `id` in the species table.
- `INSERT` / `DELETE` — Handles user interactions for adding new field notes and removing specific observations.
- `DROP TABLE IF EXISTS` — Ensures a clean database schema initialization.

---




## Sample Queries

```sql
-- Fetching all observations with their matching Turkish bird names using JOIN
SELECT observations.*, species.name_tr 
FROM observations 
JOIN species ON observations.bird_id = species.id;

-- Inserting a new user observation linked to a specific bird species
INSERT INTO observations (bird_id, note) 
VALUES (?, ?);

-- Clearing the observations table upon initialization to reset the session
DELETE FROM observations;
```
## Data Sources

- [eBird](https://ebird.org) — Cornell Lab of Ornithology
- [KuşBank](https://www.kusbank.org) — DHKD Turkey
- [IUCN Red List](https://www.iucnredlist.org)
  ---


## Files
```

/
├── app.py            # Main Flask application and SQLite connection logic
├── schema.sql        # Database schema (CREATE TABLE & relationships)
├── bird_atlas.db     # Compiled SQLite database containing species data
├── templates/
│   └── index.html    # Frontend interface with dynamic search functionality
└── README.md         # Project documentation
```

