from django.core.management.base import BaseCommand
from dbfread import DBF
from inventory.models import Hardware, Model, EquipmentType
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from DBF files into Django models'

    def handle(self, *args, **kwargs):
        # Пути к вашим DBF файлам
        hardware_dbf = "dbfiles/HARDWARE.DBF"
        model_dbf = "dbfiles/MODEL.DBF"
        typeequip_dbf = "dbfiles/TYPEEQU.DBF"

        # Очистить существующие данные при необходимости
        Hardware.objects.all().delete()
        Model.objects.all().delete()
        EquipmentType.objects.all().delete()

        # Импорт EquipmentType
        typeequip_table = DBF(typeequip_dbf, ignore_missing_memofile=True)
        typeequip_dict = {}
        for record in typeequip_table:
            equipment_type = EquipmentType.objects.create(name=record['NAME'])
            typeequip_dict[record['TYPEEQUID']] = equipment_type

        # Импорт Model
        model_table = DBF(model_dbf, ignore_missing_memofile=True)
        model_dict = {}
        for record in model_table:
            equipment_type = typeequip_dict.get(record['TYPEEQUID'])
            if equipment_type:
                model = Model.objects.create(name=record['NAME'], equipment_type=equipment_type)
                model_dict[record['MODELID']] = model

        # Импорт Hardware
        hardware_table = DBF(hardware_dbf, ignore_missing_memofile=True)
        for record in hardware_table:
            model = model_dict.get(record['MODELID'])
            if model:
                created_date = record['CREATED']
                if isinstance(created_date, str):
                    created_date = datetime.strptime(created_date, '%Y%m%d').date()
                Hardware.objects.create(
                    sn=record['SN'],
                    inventn=record['INVENTN'],
                    created=created_date,
                    model=model
                )

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы!'))
