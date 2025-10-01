# Zoom Automation

Automates joining Zoom meetings at scheduled times.

---

## Setup

### Clone the repository
```bash
cd "Desired_Directory"
git clone https://github.com/Skyturtl/zoom_automation.git
cd zoom_automation
python -m venv env
```

For windows:
```env\Scripts\activate```

For macOS/Linux:
```source env/bin/activate```

```bash
pip install -r requirements.txt
```

Now everythign should be installed

## Usage
First open the `join_class.py` file and adjust the zoom link and time at which you want to join at. 

Make sure the day of the week is in lowercase and fully written out, and the time of day is in 24-hour format. 

If you have multiple classes, feel free to add the line `schedule.every().wednesday.at("HH:MM").do(open_zoom_and_mute)` multiple times. 

Finally all you need to do is run 
`python join_class.py` within the cloned directory. As long as this file is running, then you will be automatically joining your zoom meetings now.
