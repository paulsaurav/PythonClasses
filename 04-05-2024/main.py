import requests
import csv

def fetch_wordpress_posts(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get data from the endpoint: ", response.status_code)
        return None
    
def parse_wordpress_posts(posts, my_csv_file):
    if posts is not None:
        with open(my_csv_file, 'w' , newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Content', 'Date', 'Author', 'URL'])
            for post in posts:
                print("Title", post['title'])
                print("Content", post['content'])
                print("Date", post['date'])
                print("Author", post['author'])
                print("Post URL: ", post['link'])
                title = post['title']
                content = post['content']
                date = post['date']
                author = post['author']
                post_url = post['link']
                writer.writerow([title, content, date, author, post_url])
        print("Data successfully stored in: ", my_csv_file)
        

    else:
        print("No post available to parse")

if __name__ == "__main__":
    wordpress_url = "https://teamkarimganj.com/wp-json/wp/v2/posts"
    my_csv_file = "our_posts.csv"
    posts = fetch_wordpress_posts(wordpress_url)
    parse_wordpress_posts(posts,my_csv_file)


