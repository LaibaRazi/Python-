from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver (adjust this path)
chrome_driver_path = '/Users/laibarazikhan/Desktop/chromedriver'  # Replace YourUsername with your actual username

# URL of the YouTube video you want to loop
youtube_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Replace with your desired video URL

# Number of times to play the video
loop_count = 5

# Duration to play the video (in seconds)
video_duration = 120  # Replace with the length of your video

# Setup Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Loop to play the video multiple times
for i in range(loop_count):
    print(f"Playing video {i+1}/{loop_count}")
    
    # Open YouTube video
    driver.get(youtube_url)
    
    # Wait for the video to load
    time.sleep(5)
    
    # Play the video if autoplay is off (YouTube might pause the video)
    play_button = driver.find_element(By.CLASS_NAME, 'ytp-play-button')
    if play_button:
        play_button.click()
    
    # Let the video play for the specified duration
    time.sleep(video_duration)
    
    # Refresh the page to replay the video
    driver.refresh()

# Close the browser after looping through the video
driver.quit()
