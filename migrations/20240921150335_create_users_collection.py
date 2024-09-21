from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        users_collection = self.db['users']
        users_collection.create_index('email', unique=True)
        print("Coleção 'users' criada com sucesso")

    def downgrade(self):
        self.db.drop_collection('users')
        print("Coleção 'users' removida com sucesso")
