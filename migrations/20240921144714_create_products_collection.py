from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        products_collection = self.db['products']
        products_collection.create_index('name', unique=True)
        print("Coleção 'products' criada com sucesso")

    def downgrade(self):
        self.db.drop_collection('products')
        print("Coleção 'products' removida com sucesso")
