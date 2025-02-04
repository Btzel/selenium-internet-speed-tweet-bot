# Internet Speed Tweet Bot
A Python automation tool that tests internet speed and tweets results to your ISP using Selenium WebDriver.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-red)
![Speed](https://img.shields.io/badge/Speed-Test-green)
![X](https://img.shields.io/badge/X-Integration-orange)

## 🎯 Overview
Automates internet speed monitoring by:
1. Running speed tests
2. Comparing against promised speeds
3. Logging into X (Twitter)
4. Posting results automatically
5. Tagging internet provider

## 🤖 Bot Features
### Speed Testing
- Automated Speedtest.net testing
- Download speed monitoring
- Upload speed verification
- Results extraction
- Performance comparison

### X Platform Integration
- Automated login
- Dynamic tweet composition
- Result formatting
- Automated posting
- Provider feedback

## 🔧 Technical Components
### Speed Test Implementation
```python
def get_internet_speed(self):
    self.driver.get(SPEED_TEST_WEBSITE)
    start_speed_test = self.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,'span[class="start-text"]')
    ))
    start_speed_test.click()
    result_link = (self.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,'div[data-result-id="true"] a')
    )).get_attribute("href"))
```

### Key Features
1. **Speed Monitoring**
   - Automated testing
   - Results collection
   - Speed comparison
   - Performance tracking

2. **Social Integration**
   - X authentication
   - Tweet composition
   - Automated posting
   - Provider notification

3. **Data Processing**
   - Speed calculation
   - Results formatting
   - Message generation
   - Provider feedback

## 💻 Implementation Details
### Class Structure
- `InternetSpeedXBot`: Core automation class
  - Speed testing
  - X platform interaction
  - Result processing
  - Tweet composition

### Process Flow
- Speed test execution
- Results comparison
- X authentication
- Tweet generation

## 🚀 Usage
1. Install dependencies:
```bash
pip install selenium
```

2. Set environment variables:
```bash
export EMAIL="your_x_email"
export PASSWORD="your_x_password"
export USERNAME="your_x_username"
```

3. Configure speed thresholds:
```python
PROMISED_DOWNLOAD_SPEED = 100
PROMISED_UPLOAD_SPEED = 20
```

4. Run the bot:
```bash
python main.py
```

## 🎯 Operation Rules
1. Set provider promises
2. Run speed test
3. Process results
4. Post feedback
5. Monitor responses

## 🛠️ Project Structure
```
speed-tweet-bot/
├── main.py           # Entry point
└── x_platform.py     # Bot implementation
```

## 📊 Features
### Speed Testing
- Automated test execution
- Results extraction
- Performance comparison
- Data validation

### X Integration
- Secure authentication
- Dynamic content
- Automated posting
- Response tracking

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL