
# Discussion Forum

This Discussion Forum is a comprehensive web platform developed during an internship at South Eastern Coalfields Limited (SECL). This forum serves as a dynamic space for employees to engage in discussions, share insights, and collaborate on various topics. Built using Django framework and utilizing SQLite for data management, the forum includes features such as user authentication, responsive design, and robust functionalities. It aims to foster knowledge sharing, enhance team communication, and promote community interaction within SECL.


## Authors

- [@sonaliiiiiiiiii](https://github.com/sonaliiiiiiiiii)


## Tech Stack

**Backend Framework**: Django, a high-level Python web framework known for its efficiency and scalability.

**Database**: SQLite, chosen for its simplicity and ease of integration with Django. It's suitable for development and small-scale deployments.

**Frontend**: HTML5, CSS3, and JavaScript for the user interface and dynamic interactions.

**Deployment**: Configured for local deployment. Instructions provided in the setup guide.


## Features

- **User Authentication**: Secure login and registration system to protect user accounts and data.

- **Post Questions**: Employees can post questions related to their work, projects, or any relevant topics within SECL.

- **Provide Answers**: Users can contribute answers to questions, sharing their knowledge and expertise.

- **Voting System**: Upvote and downvote functionality for answers to highlight the most helpful responses.

- **User Profiles**: Each user has a profile that showcases their activity, questions asked, and answers provided.

- **Responsive Design**: The forum is designed to be responsive, ensuring usability across devices and screen sizes.

## Deployment

To deploy the QNA discussion forum locally, follow these steps:

**Prerequisites**
- Python 3.x installed on your system.
- Pip package manager.
**Setup Instructions**
1. Clone the Repository

```bash
git clone <repository_url>
cd qna/
```
2. Install Dependencies

```bash
pip install -r requirements.txt
```
3. Run Migrations

```bash
python manage.py migrate
```
4. Create a Superuser
```bash
python manage.py createsuperuser
```
5. Start the Development Server

```bash
python manage.py runserver
```

6. Access the Application
Open your web browser and navigate to http://127.0.0.1:8000 to start using the Discussion forum locally.

## Screenshots
**Landing Page**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/5442be80-0681-4652-9881-f8b31953285c)

**Login Page**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/a2b1c6cb-d496-4cc1-9d10-7d0b589f0af6)

**Signup**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/e23d4466-ee36-4291-a11e-8f318f8527eb)

**Post or view questions**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/947069f4-2bf1-4adb-9a13-42cbc66e8d3c)

**Post Questions**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/7f6e31f7-c1b0-42be-a4a7-edfabeae98d8)

**All Questions**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/707bcd11-3805-45d9-9c30-9608024efa61)

**Answer the questions and vote**
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/21295bc1-900f-4ab4-8444-9d10cbc066b1)
![image](https://github.com/sonaliiiiiiiiii/SECL-discussion-forum/assets/125906743/91ba5e1a-ac23-4b4d-9b67-050aa809b6d3)


## Usage/Examples

**Login or Register**: Use the provided login form to access the forum or register as a new user.

**Ask Questions**: Post new questions to seek answers from colleagues and peers.

**Answer Questions**: Contribute by providing answers to posted questions.

**Vote on Answers**: Use the voting system to endorse helpful answers and prioritize valuable contributions.

**Logout**: Securely log out from your session when done.


## Support

For support, feedback, or suggestions related to the Discussion forum, please contact [sos.glu16@outlook.com]. Contributions to the project are welcome via pull requests on GitHub.


## Acknowledgements

I extend my sincere thanks to South Eastern Coalfields Limited for giving me the opportunity to develop and enhance the Discussion Forum during my internship. Special appreciation to my mentor Mr. Harshit Joshi for guiding and supporting me throughout the project.

