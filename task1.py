# Importing required dependencies
import pandas as pd
import os
import undetected_chromedriver as uc

def extract_data():
    loc=os.getcwd()
    os.mkdir("images") # If already exist please comment this line.
    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)
    driver.get('https://dermnetnz.org/image-library')
    ls=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Disease_name=[]
    Disease_url=[]
    Disease_image_url=[]
    for i in ls:
        try:
            head=driver.find_elements("xpath",f'//div[@data-leter="{i}"]/child::div[2]/div/a[@class="imageList__group__item"]')
            images=driver.find_elements("xpath",f'//div[@data-leter="{i}"]/child::div[2]/div/a[@class="imageList__group__item"]/div/img')
            diseases=[h.text for h in head]
            Disease_name.extend(diseases)
            urls=[l.get_attribute("href") for l in head]
            Disease_url.extend(urls)
            image_urls=[i.get_attribute("src") for i in images]
            Disease_image_url.extend(image_urls)
            driver.close
        except:
            pass
    df=pd.DataFrame({'Disease_name':Disease_name,'Url':Disease_url,'image_url':Disease_image_url})
    df_path=os.path.join(loc,"scraped_data.csv")
    df.to_csv(df_path,index=False)
    
    for i in range(len(df)):
        directory="images"
        download_dir=os.path.join(loc,directory)
        img_name=df['Url'][i].split('/')[-2][0:-7]+'.png'
        img_dir=os.path.join(download_dir,img_name)
        driver.get(df['image_url'][i])
        driver.save_screenshot(img_dir)    
    return print(df)


if __name__=='__main__':
    extract_data()