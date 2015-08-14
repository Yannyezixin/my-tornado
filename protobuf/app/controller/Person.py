import tornado.web
import person_pb2 as API

class PersonHandler(tornado.web.RequestHandler):
    def get(self):
        address_book = API.AddressBook()
        try:
            f = open(self.application.config['data_file'], "rb")
            address_book.ParseFromString(f.read())
            f.close()
        except IOError:
            print 'could not open file'

        persons = address_book.person

        pd = API
        self.render('list.html', persons = persons, pd = pd);

    def post(self):
        address_book = API.AddressBook()

        try:
            f = open(self.application.config['data_file'], "rb")
            address_book.ParseFromString(f.read())
            f.close()
        except IOError:
            print 'could not open file'

        person = address_book.person.add()
        person.id = int(self.get_argument('id', 0))
        person.name = self.get_argument('name', 'fuck')
        person.email = self.get_argument('email', 'null')
        number = self.get_argument('number')
        type = self.get_argument('type')
        phone_number = person.phone.add()
        phone_number.number = number

        if type == "mobile":
            phone_number.type = API.Person.MOBILE
        elif type == "home":
            phone_number.type = API.Person.HOME
        elif type == "work":
            phone_number.type = API.Person.WORK
        else:
            self.write('something error')

        try:
            f = open(self.application.config['data_file'], "wb")
            content = address_book.SerializeToString()
            f.write(content)
            f.close()
        except IOError:
            print 'can not write into file'

