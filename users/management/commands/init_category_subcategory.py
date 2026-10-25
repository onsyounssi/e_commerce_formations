from django.core.management.base import BaseCommand
# from django.db import connection
from category.models import Category, SubCategory

class Command(BaseCommand):
    help ='Initialize categories and subcategories'
    
    def handle(self, *args, **options):
        # Categories with their subcategories
        categories_data = {
            'Informatique': {
                'description': 'Produits informatiques, ordinateurs, accessoires',
                'subcategories': [
                    'Ordinateurs portables',
                    'Ordinateurs de bureau',
                    'Composants PC',
                    'Périphériques',
                    'Stockage et sauvegarde',
                    'Réseau et connectivité',
                    'Logiciels',
                    'Accessoires informatiques'
                ]
            },
            'Sport': {
                'description': 'Équipements sportifs, vêtements de sport, accessoires',
                'subcategories': [
                    'Fitness et musculation',
                    'Sports d\'équipe',
                    'Sports de raquette',
                    'Sports nautiques',
                    'Sports d\'hiver',
                    'Sports de combat',
                    'Randonnée et camping',
                    'Vélos et accessoires',
                    'Vêtements de sport',
                    'Chaussures de sport'
                ]
            },
            'Décoration': {
                'description': 'Articles de décoration intérieure et extérieure',
                'subcategories': [
                    'Luminaires',
                    'Miroirs',
                    'Cadres et tableaux',
                    'Tapis et moquettes',
                    'Rideaux et voilages',
                    'Coussins et plaids',
                    'Vases et bougeoirs',
                    'Horloges murales',
                    'Décoration murale',
                    'Objets décoratifs'
                ]
            },
            'Maison': {
                'description': 'Meubles, électroménager, ustensiles de cuisine',
                'subcategories': [
                    'Meubles de salon',
                    'Meubles de chambre',
                    'Meubles de cuisine',
                    'Électroménager',
                    'Ustensiles de cuisine',
                    'Literie',
                    'Salle de bain',
                    'Rangement et organisation',
                    'Outils de ménage',
                    'Petit électroménager'
                ]
            },
            'Véhicules': {
                'description': 'Voitures, motos, pièces détachées, accessoires auto',
                'subcategories': [
                    'Voitures particulières',
                    'Motos et scooters',
                    'Poids lourds',
                    'Pièces détachées',
                    'Accessoires auto',
                    'Entretien et lubrifiants',
                    'Pneus et jantes',
                    'GPS et électronique auto',
                    'Location de véhicules',
                    'Véhicules utilitaires'
                ]
            },
            'Vêtements': {
                'description': 'Habits, chaussures, accessoires de mode',
                'subcategories': [
                    'Vêtements hommes',
                    'Vêtements femmes',
                    'Vêtements enfants',
                    'Chaussures hommes',
                    'Chaussures femmes',
                    'Chaussures enfants',
                    'Accessoires de mode',
                    'Sacs et maroquinerie',
                    'Montres et bijoux',
                    'Vêtements professionnels'
                ]
            },
            'Biscuiterie': {
                'description': 'Biscuits, pâtisseries, produits de boulangerie',
                'subcategories': [
                    'Biscuits secs',
                    'Gâteaux',
                    'Pâtisseries',
                    'Viennoiseries',
                    'Confiseries',
                    'Chocolats',
                    'Produits de boulangerie',
                    'Ingrédients de pâtisserie',
                    'Biscuits bio et diététiques',
                    'Spécialités régionales'
                ]
            },
            'Électronique': {
                'description': 'Smartphones, tablettes, TV, appareils photo',
                'subcategories': [
                    'Smartphones',
                    'Tablettes',
                    'Télévisions',
                    'Appareils photo',
                    'Caméscopes',
                    'Audio et Hi-Fi',
                    'Accessoires électroniques',
                    'Batteries et chargeurs',
                    'Casques et écouteurs',
                    'Montres connectées'
                ]
            },
            'Beauté': {
                'description': 'Cosmétiques, soins de la peau, parfums',
                'subcategories': [
                    'Soins du visage',
                    'Soins du corps',
                    'Maquillage',
                    'Parfums',
                    'Soins capillaires',
                    'Produits naturels',
                    'Coiffure et stylisme',
                    'Épilation et soins',
                    'Parapharmacie',
                    'Accessoires beauté'
                ]
            },
            'Jardinage': {
                'description': 'Outils de jardin, plantes, équipements extérieurs',
                'subcategories': [
                    'Outils de jardin',
                    'Plantes et fleurs',
                    'Mobilier de jardin',
                    'Arrosage',
                    'Engrais et terreau',
                    'Piscine et spa',
                    'Éclairage extérieur',
                    'Motoculture',
                    'Serres et accessoires',
                    'Protection des plantes'
                ]
            },
            'Livres': {
                'description': 'Livres, magazines, bandes dessinées',
                'subcategories': [
                    'Romans et littérature',
                    'Livres scolaires',
                    'Mangas et BD',
                    'Livres pratiques',
                    'Livres jeunesse',
                    'Magazines',
                    'E-books',
                    'Livres audio',
                    'Beaux livres',
                    'Dictionnaires et encyclopédies'
                ]
            },
            'Jouets': {
                'description': 'Jeux, jouets pour enfants, puzzles',
                'subcategories': [
                    'Poupées et peluches',
                    'Jeux de société',
                    'Jeux éducatifs',
                    'Puzzles',
                    'Voitures et véhicules',
                    'Jeux de construction',
                    'Jouets d\'extérieur',
                    'Jeux vidéo',
                    'Jouets premier âge',
                    'Déguisements'
                ]
            },
            'Santé': {
                'description': 'Produits de santé, bien-être, équipement médical',
                'subcategories': [
                    'Compléments alimentaires',
                    'Vitamines et minéraux',
                    'Équipement médical',
                    'Orthopédie',
                    'Aide à la mobilité',
                    'Bien-être et relaxation',
                    'Thermomètres et tensiomètres',
                    'Soins des pieds',
                    'Aromathérapie',
                    'Homéopathie'
                ]
            },
            'Animaux': {
                'description': 'Accessoires pour animaux, nourriture, soins',
                'subcategories': [
                    'Alimentation animale',
                    'Accessoires pour chiens',
                    'Accessoires pour chats',
                    'Accessoires pour oiseaux',
                    'Aquarium et poissons',
                    'Petits animaux',
                    'Soins et hygiène',
                    'Transport et voyages',
                    'Jouets pour animaux',
                    'Accessoires d\'éducation'
                ]
            },
            'Bricolage': {
                'description': 'Outils, quincaillerie, matériaux de construction',
                'subcategories': [
                    'Outils à main',
                    'Outils électroportatifs',
                    'Quincaillerie',
                    'Matériaux de construction',
                    'Peinture et revêtements',
                    'Plomberie',
                    'Électricité',
                    'Menuiserie',
                    'Échafaudage et échelles',
                    'Équipement de protection'
                ]
            },
            'Musique': {
                'description': 'Instruments de musique, accessoires, partitions',
                'subcategories': [
                    'Guitares et basses',
                    'Pianos et claviers',
                    'Batteries et percussions',
                    'Instruments à vent',
                    'Instruments à cordes',
                    'Sonorisation',
                    'Accessoires musicaux',
                    'Partitions',
                    'Studios d\'enregistrement',
                    'Cours et méthodes'
                ]
            },
            'Bureau': {
                'description': 'Fournitures de bureau, mobilier professionnel',
                'subcategories': [
                    'Fournitures de bureau',
                    'Mobilier de bureau',
                    'Papeterie',
                    'Impression et scan',
                    'Classement et archivage',
                    'Écriture et correction',
                    'Matériel de présentation',
                    'Cartouches et toners',
                    'Accessoires informatiques pro',
                    'Matériel de reprographie'
                ]
            },
            'Bagages': {
                'description': 'Valises, sacs à dos, maroquinerie',
                'subcategories': [
                    'Valises',
                    'Sacs à dos',
                    'Sacs de voyage',
                    'Bagages à main',
                    'Accessoires de voyage',
                    'Maroquinerie',
                    'Porte-documents',
                    'Sacs d\'ordinateur',
                    'Trousse de toilette',
                    'Étiquettes et protection'
                ]
            },
            'Montres': {
                'description': 'Montres, bijoux, accessoires de luxe',
                'subcategories': [
                    'Montres classiques',
                    'Montres sport',
                    'Montres de luxe',
                    'Montres connectées',
                    'Bracelets de montre',
                    'Bagues et alliances',
                    'Colliers et pendentifs',
                    'Boucles d\'oreilles',
                    'Bracelets et chaînes',
                    'Pierres précieuses'
                ]
            },
            'Photographie': {
                'description': 'Appareils photo, objectifs, accessoires photo',
                'subcategories': [
                    'Appareils photo reflex',
                    'Appareils hybrides',
                    'Appareils compacts',
                    'Objectifs',
                    'Trépieds et supports',
                    'Flash et éclairage',
                    'Filtres et accessoires',
                    'Sacs et étuis photo',
                    'Imprimantes photo',
                    'Studio et matériel pro'
                ]
            }
        }
        
        
        # clear existing data
        self.stdout.write('Clearing existing categories and subcategories')
        SubCategory.objects.all().delete()
        Category.objects.all().delete()
        
        # create categories and subcategories
        created_categories = 0
        created_subcategories = 0
        
        for category_name, category_data in  categories_data.items():
            # create category
            category, cat_created = Category.objects.get_or_create(
                name=category_name,
                defaults={"description": category_data['description']}
            )
            
            if cat_created:
                created_categories+=1
                self.stdout.write(f'created category: {category_name}')
            
            # create subcategory
            for subcat_name in category_data['subcategories']:
                subcategory, sub_created = SubCategory.objects.get_or_create(
                    name = subcat_name,
                    category = category
                )
                if sub_created:
                    created_subcategories+=1
                    self.stdout.write(f'created subcategories: {subcat_name}')
                
        # summary
        self.stdout.write(self.style.SUCCESS(
            f'\n initialization complete! \n'
            f'Categories: {created_categories}\n'
            f'SubCategories: {created_subcategories}'
        ))
        
        # display all categories with thier subcategory count
        self.stdout.write('\nSummary by category: ')
        for category in Category.objects.all().order_by('name'):
            subcat_count = category.subcategories.count()
            self.stdout.write(f' * {category.name}: {subcat_count} subcategory')
