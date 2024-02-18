import os
class Library:
   


 def __init__(self):                   # dosya açması için constructer method oluşturuldu
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

 def __del__(self):
        self.file.close()     #  dosya kapaması için deconstructer method oluşturuldu 


 def list_books(self) -> None:    # books.txt dosyasındaki tüm kitapları listeleyen fonskiyon
        books_list = self.read_file()
        total_books = len(books_list)
        print(f"Toplam Kayıtlı Kitap Sayısı: {total_books}\n")
        print(f"{'Kitap Adı:':<20} {'Yazarı:'}")
        for book in books_list:
            book_info = book.strip().split(",")
            if len(book_info) >= 2:
                book_name = book_info[0]
                author_name = book_info[1]
                print(f"{book_name:<20} {author_name}")
            else:
                print("Geçersiz kitap bilgisi")
            print()



 def search_book(self) -> None:   # Ekstra olarak eklediğim aranılan kitabın adı girilince yazar basım tarihi ve sayfa sayısını veren fonksiyon
        print("Kitap Arama\n")
        title = input("Kitap Adı: ")
        books_list = self.search_book_from_file(title)
        if books_list:
            for book in books_list:
                print(f"Yazar: {book['authorName']}")
                print(f"Yayınlanma Tarihi: {book['releaseYear']}")
                print(f"Sayfa Sayısı: {book['pageNumber']}")
                print()
        else:
            print("Aradığınız kitap bulunamadı.")



 def add_book(self) -> None:     #book.txt dosyasına kitap kaydı ekleyen fonsksiyon
        print("Yeni Kitap Ekle")
        title = input("Kitap Adı: ")
        author_name = input("Yazarı: ")
        release_year = input("Yayın Tarihi: ")
        page_number = input("Sayfa Sayısı: ")
        book_info = f"{title},{author_name},{release_year},{page_number}\n"
        print(f"Yeni Kayıt: {book_info}")
        if self.are_you_sure():
            self.add_book_to_file(book_info)
            print("Kayıt Eklendi.\n")



 def remove_book(self) -> None:  #başlığı girilen kitabı books.txt dosyasından silen fonksiyon.
        title_param = input("Silmek istediğiniz kitabın başlığını girin: ")     
        books_list = self.read_file()
        indexes_to_remove = [index for index, book in enumerate(books_list) if title_param.upper() in book.upper()]
        if not indexes_to_remove:
            print("Belirtilen başlığa sahip bir kitap bulunamadı.")
            return
        for index in sorted(indexes_to_remove, reverse=True):
            del books_list[index]
        with open("books.txt", "w") as file_object:
            file_object.truncate(0)
        self.write_file(books_list)
        print(f"'{title_param}' başlıklı kitap başarıyla silindi.")



 def are_you_sure(self) -> bool:  #herhangi bir işlem yapmadan önce onay isteyen fonskiyon.
        while True:
            answer = input("Emin misiniz? (E)vet/(H)ayır ")
            print()
            if answer.upper() == "E":
                return True
            elif answer.upper() == "H":
                return False



 def read_file(self) -> list:  #"books.txt" adlı dosyayı okumak için oluşturuldu.
        if os.path.isfile("books.txt"):
            with open("books.txt", "r") as file_object:
                books_list = file_object.readlines()
        else:
            books_list = []
        return books_list



 def write_file(self, books_list_param: list) -> None:  # kitap listesini "books.txt" dosyasına yazmak için oluşturuldu.
        with open("books.txt", "w") as file_object:
            file_object.writelines(books_list_param)



 def add_book_to_file(self, book_info: str) -> None:  # "book_info" parametresi olarak verilen yeni bir kitap bilgisini "books.txt" dosyasına ekler.
        books_list = self.read_file()
        books_list.append(book_info)
        self.write_file(books_list)



 def search_book_from_file(self, title_param: str) -> list: #"title_param" parametresi olarak verilen kitap başlığına sahip kitabı "books.txt" dosyasından arar.
        books_list = self.read_file()
        response_list = []
        for book in books_list:
            book_info = book.strip().split(",")
            if book_info[0].upper() == title_param.upper():
                response_list.append({
                    "title": book_info[0],
                    "authorName": book_info[1],
                    "releaseYear": book_info[2],
                    "pageNumber": book_info[3]
                })
        return response_list



 def delete_all_records(self) -> None: #menüde olmayan basitçe tüm kayıtları books.txt dosyasından silmek için kullanılan foksiyon.
        confirm = input("Tüm kitap kayıtlarını silmek istediğinize emin misiniz? (E)vet/(H)ayır: ")
        if confirm.upper() == "E":
            with open("books.txt", "w") as file_object:
                file_object.truncate(0)
            print("Tüm kitap kayıtları silindi.\n")
        else:
            print("İşlem iptal edildi.\n")




if __name__ == "__main__":
    lib = Library() 
    while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Search Book")
        print("5) Exit")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice=="4":
            lib.search_book()
        elif choice == "5":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
