import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys

URL = "https://cookpad.com"


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード
    # options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
    # options.add_argument("--enable-javascript")  # JS無効
    return options


def search_by_food(driver, food):
    driver.get(f"{URL}")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "keyword").send_keys(food)
    driver.find_element(By.ID, "submit_button").click()

    time.sleep(5)


def get_recipes(driver):
    recipe_previews = driver.find_elements(By.CLASS_NAME, 'recipe-preview')

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element(By.CLASS_NAME, 'recipe-title').text
        recipe_url = recipe_preview.find_element(By.CLASS_NAME, 'recipe-title').get_attribute('href')

        recipes.append({
            "title": recipe_title,
            "url": URL + recipe_url})

    return recipes


def main():
    food = 'トマト'

    # Close忘れ防止にwithを使用する
    with webdriver.Chrome(options=chromedriver_options()) as driver:
        search_by_food(driver, food)
        # 抽出情報をモジュールに渡す
        recipes = get_recipes(driver)

        for recipe in recipes:
            print(f"レシピ名 {recipe['title']}, URL:{recipe['url']}")


if __name__ == '__main__':
    main()
