# programmieren_2_aufgabe_1
This repo contains the code for exercise 1.

Fictitious sensor data is imported from a CSV-file into a numpy array. This array is sorted via a selfcreated bubble sort algorithm and finally visualized via a matplotlib plot. The plot can be safed to the folder "figures" as PNG-file. (using power_curve.py)

---

### Requirements

- Python 3.12 or newer
- Git
- Internet connection for installing dependencies
- PDM 2.26 or newer

to install PDM, follow the instructions on the official project website: https://pdm-project.org/

---

### Clone the Project

Clone the repository:

```bash
git https://github.com/MarcWechselberger/programmieren_2_aufgabe_1.git
cd programmieren_2_aufgabe_1
```

---

### Install Dependencies

Install all required packages:

```bash
pdm install
```

This will:

- install all Python dependencies
- create a virtual environment
- use the versions defined in `pdm.lock`

---

### Example plot

![Hier sollte jetzt ein Plot sein!](/figures/NewFigure.png)

---

### Project Structure

```text
programmieren_2_aufgabe_1/
│
├── figures/
│   └── NewFigure.png
│       
├── activity.csv
├── power_curve.py
├── load_data.py
├── sort.py
├── pyproject.toml
├── pdm.lock
└── README.md
```

---

### License

No License

---

### Authors

Nicolas Unterweger   
Emmanuel Tilg   
Marc Wechselberger   
GitHub: https://github.com/MarcWechselberger

