from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas.contact import ContactModel


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def get_contacts(self, skip: int = 0, limit: int = 100, q: str | None = None):
        return await self.repository.get_contacts(skip, limit, q)

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact(contact_id)

    async def create_contact(self, body: ContactModel):
        return await self.repository.create_contact(body)

    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.repository.update_contact(contact_id, body)

    async def delete_contact(self, contact_id: int):
        return await self.repository.delete_contact(contact_id)

    async def get_birthdays(self, days: int):
        return await self.repository.get_birthdays(days)
