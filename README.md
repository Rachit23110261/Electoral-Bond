# Electoral-Bond
Describes data from datasets of electoral bonds between different companies and different political parties
Creating a README file for your project is a great way to provide instructions on how to use your code. Here's an example of an elaborate README file for your Flask MySQL project:
# Flask MySQL Project
This project demonstrates how to use Flask with MySQL to create a web application for managing political party donations.
## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required packages:

   ```bash
   pip install Flask flask-mysqldb
   ```

3. Set up your MySQL database:
   
   - Create a new database named `website`.
   - Update the MySQL configuration in `app.py` with your MySQL username and password.

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- **Main Page:** Access the main page to view the available options.
- **Search for Bond Number (a_1):** Enter a Bond Number to search for details.
- **Search by Party (a_2):** Select a political party and enter a search term to find details.
- **Total Denominations by Date (a_3):** Select a political party to view total denominations by date.
- **Total Denominations by Purchaser (a_4):** Enter a purchaser name to view total denominations by purchase date.
- **Find Purchasers by Bond Number (a_5):** Enter a party name to find purchasers by bond number.
- **Find Parties by Purchaser (a_6):** Enter a purchaser name to find parties by purchaser.

## Screenshots
### Q1
/a_1 (Search by Bond Number):
Description: This route allows users to search for details based on a specific Bond Number.
![Screenshot 2024-04-23 221909](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/8621fd1e-ad17-4266-891b-0915d1bf62a8)


Description: This route enables users to search for details based on a selected filter.
![Screenshot 2024-04-23 221939](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/8b4dd835-39a8-46d3-8436-bb9393137a59)


### Q2
/a_3 (Total Denominations by Date):
Description: This route displays the total denominations for a selected political party grouped by date of encashment.
![Screenshot 2024-04-23 221958](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/8e185c0c-ec32-42ff-8cd7-b2705388e6ae)
Bar graph
![Screenshot 2024-04-23 222015](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/3b2327c5-42b5-4e3e-80a6-3324658d4889)


### Q3
/a_4 (Total Denominations by Purchaser):
Description: This route shows the total denominations for a selected purchaser grouped by date of purchase.
![Screenshot 2024-04-23 222057](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/6d92253e-62b9-4ac3-b91d-10e6b1519130)
bargraph
![Screenshot 2024-04-23 222121](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/f2045607-43d3-4cf5-914b-686518a241da)


### Q4
/a_5 (Find Purchasers by Bond Number):
Description: This route allows users to find purchasers based on a selected party's bond number.
![Screenshot 2024-04-23 222908](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/f917a68d-9435-446c-96bf-8757ae176da6)


### Q5
/a_6 (Find Parties by Purchaser):
Description: This route enables users to find political parties based on a selected purchaser's name.
![Screenshot 2024-04-23 222821](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/87521ce3-3f32-43c6-a781-7f16120ff535)

### Q6
![Screenshot 2024-04-23 230323](https://github.com/Rachit23110261/Electoral-Bond/assets/143380758/ced9908f-2b91-4dfc-acb6-6930c51c1203)


## Technologies Used

- Flask
- MySQL
- Chart.js
- HTML/CSS

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Modify this template to include specific details about your project, such as screenshots, additional features, and any special setup instructions.
