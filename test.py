from freesteel.common import get_default_reader
from freesteel.card import CardCommand
from freesteel.eid_card import CardFile, EidCard, PersonalField, DocumentField

reader = get_default_reader()
card = reader.wait_for_card()
eid_card = EidCard(card)
personal = eid_card.get_personal()
print(personal)
document = eid_card.get_document()
print(document)
residence = eid_card.get_residence()
print(residence)
photo = eid_card.get_photo()
with open("image.jpeg", 'wb+') as jpeg_file:
    jpeg_file.write(photo)
card.disconnect()
