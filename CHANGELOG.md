```markdown
# 📜 Changelog  
All notable changes to this project will be documented in this file.  

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
and this project adheres to [Semantic Versioning](https://semver.org/).  

---

## [1.0.0] - 2025-08-12  
### Added  
- Initial release of **Data Preparation API**.  
- Implemented dataset **scaling** options: `standard`, `minmax`, `robust`.  
- Implemented dataset **encoding** options: `onehot`, `label`.  
- Implemented **train-test splitting** with optional stratification.  
- Added request validation using **Pydantic models**.  
- Added **file upload support** (CSV/Excel) via shared directory or API parameter.  
- Outputs prepared datasets and metadata to `/prepared_files`.  

---
