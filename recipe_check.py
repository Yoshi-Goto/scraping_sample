import requests as requests
import bs4


def search_recipes(base_url, food):
    response = requests.get(f"{base_url}/search/{food}")
    html = response.text
    return html


def get_recipes(base_url, html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    recipe_previews = soup.find_all(class_="recipe-preview")

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find(class_="recipe-title").text
        recipe_url = recipe_preview.find(class_="recipe-title").attrs['href']

        recipes.append({
            "title": recipe_title,
            "url": f"{base_url}{recipe_url}"})
    return recipes


def main():
    base_url = 'https://cookpad.com'
    food = 'トマト'

    html = search_recipes(base_url, food)
    recipes = get_recipes(base_url, html)

    for recipe in recipes:
        print(f"レシピ名 {recipe['title']}, URL:{recipe['url']}")


if __name__ == '__main__':
    main()
