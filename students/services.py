import random
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from departments.models import Department
from students.models import Student


def get_or_create_students():
    first_names = """
    Shefqet, Alban, Dibran, Fatime, Selime, Aida, Klejda, Mimoza, Zana, Ariana, Theofan, Bujar, Visar, Altin, Kadrush, 
    Kristë, Anton, Faton, Labinot, Drita, Iliriana, Shtjefën, Sherafedin, Alaudin, Gjergj, Lekë, Floriana, Vjosa, Suzana, 
    Fatos, Petraq, Ilir, Salih, Ibrahim, Hashim, Enkela, Jeta, Marenglen, Enver, Fidan, Korab, Alma, Arta, Kastriot, Stakë, 
    Bedri, Zylfiqefli, Lutfi, Luigj, Shefkije, Alije, Lejla, Ibish, Ndue, Miranda, Fron, Sherafedin, Bora, Shkëndije, 
    Patriot, Trim, Aldo, Ridvan, Shyqri, Paskal, Zeqir, Robert, Gani, Ardit, Shinasi, Sandër, Redon, Saranda, Ragip, Afrim,
     Gëzim, Besim, Bajram, Shkenca, Flamur, Veton, Halit, Xhavit, Ramush, Enkela, Jeta, Liridon, Irena, Hysnije, Elena, 
     Rifadije, Fllanza, Mariza, Melihate, Shqipe, Kosovare, Abetare, Shqiptare.
    """

    last_names = """
    Hoxha ,Shehu ,Prifti ,Çela ,Leka ,Dervishi ,Hysi ,Rama ,Dibra ,Abazi ,Sinani ,Gjika ,Kola ,Kraja ,Luka ,Duka ,Gjoka
    ,Murati ,Kristi ,Mulo ,Muço ,Andoni ,Hasani ,Koçi ,Frashëri ,Ruçi ,Zeneli ,Papa ,Spahiu ,Balla ,Bushati ,Gjoni ,Brahimi
    ,Kanani ,Alikaj ,Arapi ,Çaushi ,Halili ,Thanasi ,Xhafa ,Aliaj ,Basha ,Mezini ,Sula ,Agolli ,Gjata ,Haxhiu ,Jaho ,Kodra
    ,Lako ,Mehmeti ,Niko ,Osmani ,Pano ,Bardhi ,Cani ,Deda ,Demiri ,Hasa ,Kasa ,Mema ,Myftiu ,Peçi ,Shtylla ,Toska ,Treska
    ,Ymeri ,Zaimi ,Bezhani ,Dedja ,Duro ,Kamberi ,Kote ,Laçi ,Laze ,Malaj ,Marku ,Hana ,Shyti ,Skënderi ,Berberi ,Dede
    ,Elezi ,Gjergji ,Jakupi ,Koka ,Kondi ,Luarasi ,Vata ,Meçe ,Nikolla ,Rexha ,Saraçi ,Xhani ,Dangëllia ,Shalsi ,Madhi
    ,Begu ,Myslimi , Kaleshi
    """

    first_names = first_names.split(',')
    last_names = last_names.split(',')
    departments = Department.objects.all()
    students_data = [
        (random.choice(first_names), random.choice(last_names), random.choice(departments)) for i in range(500)
    ]
    students = [Student(first_name=fn.strip(), last_name=ln.strip(), department=d) for fn, ln, d in students_data]
    students = Student.objects.bulk_create(students)
    return students


def create_permissions():
    content_type = ContentType.objects.get_for_model(Student)
    Permission.objects.get_or_create(
        codename='view_students',
        name='Can view student list',
        content_type=content_type
    )
