# 🐦 Turkey Bird Atlas — SQL Project

**Course:** Applied SQL — Uygulamalı SQL
**Student:** Arda Taştan | 24025019 | Department of Mathematics, Yıldız Technical University

---

## About

A relational SQL database that stores and organizes data about bird species found in Turkey. The database includes species names (Turkish & Latin), family, migration status, IUCN conservation status, habitat types, regional distribution, and field observations with GPS coordinates.

---

## Database Schema

6 tables connected by primary and foreign keys:

| Table | Description |
|---|---|
| `species` | Main info for each bird species |
| `habitats` | Habitat types (wetland, forest, steppe, coast, mountain) |
| `regions` | All 81 Turkish provinces with geographic zone |
| `species_habitat` | Which species live in which habitats (many-to-many) |
| `species_region` | Which species are found in which regions (many-to-many) |
| `observations` | Field sightings with date, GPS, and observer info |

---

## SQL Features Used

- `JOIN` (INNER, LEFT) — combine data from multiple tables
- `VIEW` — reusable queries for species summary and map display
- `GROUP BY` / `HAVING` — aggregate observations by region or species
- `CTE` — readable multi-step queries for species profiles
- `CHECK` / `ENUM` — validate conservation and migration status values
- `INDEX` — faster filtering on commonly queried columns

---

## Sample Queries

```sql
-- Threatened species only
SELECT name_tr, name_latin, conservation_status
FROM species
WHERE conservation_status IN ('VU', 'EN', 'CR');

-- Observation count per region
SELECT r.city_name, COUNT(*) AS total_observations
FROM observations o
JOIN regions r ON o.region_id = r.region_id
GROUP BY r.city_name
ORDER BY total_observations DESC;
```

---

## Data Sources

- [eBird](https://ebird.org) — Cornell Lab of Ornithology
- [KuşBank](https://www.kusbank.org) — DHKD Turkey
- [IUCN Red List](https://www.iucnredlist.org)

---

## Files

```
/
├── schema.sql        # CREATE TABLE statements
├── seed_data.sql     # Sample INSERT data
├── queries.sql       # Example queries
└── README.md
```# Turkey-s-Bird-Atlas
