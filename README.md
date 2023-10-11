
# Healitia 
![Logo](https://demo.mehdirezakhani.ir/_next/static/media/HLogo.25be5cbf.png)

Healitia is a digital health startup that is developing a platform to help elderly patients manage their health and wellness with the help of AI. The platform will offer a variety of features, including:
- Health and fitness calculators
- Personal health record
- Symptom tracker
- Medication reminder
- Auto pathology
- Medical exam data analysis
- Chatbot
- Library of healthy recipes and Corrective exercises

Healitia's mission is to raise awareness and make it easier for elderly people to manage their health and wellness. This startup believes that everyone should have access to high-quality, affordable healthcare.

# How Healitia can help elderly patients

Healitia can help elderly patients in a number of ways, including:

- Making it easier to track their health and wellness data
- Helping them to identify and manage their health risks
- Providing them with personalized recommendations for improving their health and well-being
- Connecting them with healthcare providers and other resources

# Roadmap
Healitia is currently in the development stage, and its first version will be released in December 2023. The platform will initially be available as a web application, but mobile native applications for Android and iOS will be developed in the future.

# Conclusion
Healitia is a promising new digital health platform that has the potential to make a significant difference in the lives of elderly patients. By providing them with the tools and resources they need to manage their health and wellness, Healitia can help them to live longer, healthier, and more independent lives.


## Authors

- [Mehdi Rezakhani](https://github.com/MehdiiRezakhani) -  Front-End Developer
- [Elham Sharifia](https://github.com/el-sh200) -  Back-End Developer


## Live Version

[Web-Application](https://healitia.ir/)

[Back-end](https://api.healitia.ir/)


## Tech Stack

**Client:** Next, React, Context API, TailwindCSS, Material-UI

**Server:** Django, Django Rest Framework, Postgresql

*[Liara](https://liara.ir/) services were used to deploy the project on a server.


## Related

[Front-End Source](https://github.com/MehdiiRezakhani/Healitia_WebApp)

[Back-End Source](https://github.com/el-sh200/healitia)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Primary Color | ![#3A8EF6](https://via.placeholder.com/10/3A8EF6?text=+) #3A8EF6 |
| Secondary Color | ![#e1e2e3](https://via.placeholder.com/10/e1e2e3?text=+) #e1e2e3 |
| Light Color | ![#f7fafe](https://via.placeholder.com/10/f7fafe?text=+) #f7fafe |
| Dark Color | ![#111](https://via.placeholder.com/10/111?text=+) #111 |
| Error Color | ![#ef8481](https://via.placeholder.com/10/ef8481?text=+) #ef8481 |
| Success Color | ![#00ba88](https://via.placeholder.com/10/00ba88?text=+) #00ba88 |




## Features

- Light/dark mode toggle
- Live previews
- SPA & PWA


## Run Locally

Clone the project

```bash
  git clone https://github.com/el-sh200/healitia
```

Go to the project directory

```bash
  cd healitia
```

Create your own virtual environment

```bash
  virtualenv venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Generate a new secret key


Migrate your migrations

```bash
  $ python manage.py migrate
```

Create a new superuser

```bash
  python manage.py createsuperuser
```

Final checks
```bash
  python manage.py runserver
```