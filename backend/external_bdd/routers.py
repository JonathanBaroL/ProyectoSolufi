class ExternalDBRouter:
    app_label = {'backend', 'external_bdd'}
    def db_for_read(self, model, **hints): 
        if model._meta.app_label in self.app_label: 
            return 'external_db' 
        return None 
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.app_label:
            return 'external_db'  # Utiliza la base de datos 'external_db' para los modelos de la app
        return None  # No cambia la base de datos por defecto para operaciones de escritura

    def allow_relation(self, obj1, obj2, **hints):
        return None  # No permite relaciones entre bases de datos diferentes

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'external_db':
            return app_label in self.app_label  # Solo permite migraciones para la aplicación 'external_bdd' en la base de datos 'external_db'
        return None  # No permite migraciones en otras bases de datos
