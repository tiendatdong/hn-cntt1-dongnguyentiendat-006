class MovieTicket:
    def __init__(self, id, customer_name, movie_name, ticket_price, quantity, discount, revenue_type):
        self.id = id
        self.customer_name = customer_name
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.quantity = quantity
        self.discount = discount
        self.revenue_type = revenue_type

    def calculate_revenue(self):
        revenue = (self.ticket_price * self.quantity) - self.discount
        return revenue

    def classify_revenue(self):
        revenue = self.calculate_revenue()
        if revenue < 100000:
            self.revenue_type = "Thấp"
        elif 100000 <= revenue < 500000:
            self.revenue_type = "Trung bình"
        else:
            self.revenue_type = "Cao"

    def display_info(self):
        print(f"Mã vé: {self.id}")
        print(f"Tên khách hàng: {self.customer_name}")
        print(f"Tên phim: {self.movie_name}")
        print(f"Giá vé: {self.ticket_price}")
        print(f"Số lượng vé: {self.quantity}")
        print(f"Giảm giá: {self.discount}")
        print(f"Doanh thu: {self.calculate_revenue()}")
        print(f"Loại doanh thu: {self.revenue_type}")
class MovieTicketManager:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        print("Thêm vé xem phim thành công")

    def show_all(self):
        if not self.tickets:
            print("Danh sách vé xem phim trống")
        else:
            for ticket in self.tickets:
                ticket.display_info()

    def update_ticket(self, id, ticket_price, quantity, discount):
        for ticket in self.tickets:
            if ticket.id == id:
                ticket.ticket_price = ticket_price
                ticket.quantity = quantity
                ticket.discount = discount
                ticket.calculate_revenue()
                ticket.classify_revenue()
                return True
        return False

    def delete_ticket(self, id):
        for i, ticket in enumerate(self.tickets):
            if ticket.id == id:
                del self.tickets[i]
                return True
        return False

    def search_ticket(self, name_customer=None, name_movie=None):
        results = []
        for ticket in self.tickets:
            if name_customer and name_customer.lower() in ticket.customer_name.lower():
                results.append(ticket)
            elif name_movie and name_movie.lower() in ticket.movie_name.lower():
                results.append(ticket)
        return results
while True:
    print("================ MENU ================")
    print("1. Hiển thị danh sách vé xem phim")
    print("2. Thêm vé xem phim mới")
    print("3. Cập nhật vé xem phim")
    print("4. Xóa vé xem phim")
    print("5. Tìm kiếm vé xem phim")
    print("6. Thoát chương trình")
    try:
        choice = input("Nhập lựa chọn của bạn: ")
    except ValueError:
        print("Lựa chọn không hợp lệ")
        continue
    if choice == "1":
        manager = MovieTicketManager()
        manager.show_all()
    if choice == "2":
        id = input("Nhập mã vé: ").strip().upper()
        customer_name = input("Nhập tên khách hàng: ").strip().title()
        movie_name = input("Nhập tên phim: ").strip().title()
        manager = MovieTicketManager()
        while True:
            try:
                ticket_price = int(input("Nhập giá vé xem phim: "))
                if ticket_price < 0:
                    print("Số tiền vé phim không hợp lệ")
                    continue
                break
            except ValueError:
                print("Giá vé phải là một số nguyên")
        while True:
            try:
                quantity = int(input("Nhập số lượng vé: "))
                if quantity < 1 or quantity > 100:
                    print("Số lượng vé phải là số nguyên từ 1 đến 100")
                    continue
                break
            except ValueError:
                print("Số lượng vé phải là một số nguyên")
        while True:
            try:
                discount = float(input("Nhập giảm giá: "))
                if discount < 0:
                    print("Giảm giá phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Giảm giá phải là một số thực")
        ticket = MovieTicket(id, customer_name, movie_name, ticket_price, quantity, discount, "")
        ticket.calculate_revenue()
        ticket.classify_revenue()
        manager.add_ticket(ticket)
    if choice == "3":
        id = input("Nhập mã vé cần cập nhật: ").strip().upper()
        if not id:
            print("Không tìm thấy mã vé cần cập nhật")
        else:
            while True:
                price_ticket = int(input("Nhập giá vé xem phim mới: "))
                if price_ticket < 0:
                    print("Số tiền vé phim không hợp lệ")
                else:
                    break
            while True:
                quantity = int(input("Nhập số lượng vé mới: "))
                if quantity < 1 or quantity > 100:
                    print("Số lượng vé phải là số nguyên từ 1 đến 100")
                else:
                    break
            while True:
                discount = float(input("Nhập giảm giá mới: "))
                if discount < 0:
                    print("Giảm giá phải lớn hơn hoặc bằng 0")
                else:
                    break
            manager = MovieTicketManager()
            manager.update_ticket(id, price_ticket, quantity, discount)
            print("Cập nhật vé xem phim thành công")
    if choice == "4":
        id = input("Nhập mã vé cần xóa: ").strip().upper()
        if not id:
            print("Không tìm thấy mã vé cần xóa")
        else:
            choose = input("Bạn có chắc chắn muốn xóa vé xem phim này không? (y/n): ").strip().lower()
            if choose != "y":
                print("Hủy xóa vé xem phim")
                continue
            manager = MovieTicketManager()
            manager.delete_ticket(id)
            print("Xóa vé xem phim thành công")
    if choice == "5":
        while True:
            print("Tìm kiếm vé xem phim")
            print("1. Tìm kiếm theo tên khách hàng")
            print("2. Tìm kiếm theo tên phim")
            try:
                choose = input("Nhập lựa chọn của bạn: ")
            except ValueError:
                print("Lựa chọn không hợp lệ")
                continue
            if choose == "1":
                name_cus = input("Nhập tên khách hàng bạn muốn tìm kiếm: ").strip().title()
                manager = MovieTicketManager()
                results = manager.search_ticket(name_customer=name_cus)
            elif choose == "2":
                name_mov = input("Nhập tên phim bạn muốn tìm kiếm: ").strip().title()
                manager = MovieTicketManager()
                results = manager.search_ticket(name_movie=name_mov)
            else:
                print("Lựa chọn không hợp lệ")
                continue

            if results:
                print("Kết quả tìm kiếm:")
                for ticket in results:
                    ticket.display_info()
            else:
                print("Không tìm thấy vé xem phim phù hợp")

    if choice == "6":
        print("Thoát chương trình.....")
        break