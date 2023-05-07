# from typing import Type, Dict, Union
# from src.infra.interface import ResponsabilityInterface, AnimalStrategyInterface

# from src.domain.models import Animals:  não deve acessar domain

# Devem ser interfaces recebidas
# Infra só implementa interfaces de "data"
# from src.data.strategies.animals import (
#     HenStrategy,
#     DogStrategy,
#     CattleStrategy,
#     PigStrategy,
#     HorseStrategy
# )
# from src.data.validators.animals import (
#     HenValidator,
#     DogValidator,
#     CattleValidator,
#     PigValidator,
#     HorseValidator
# )

# Essa Implementação deve extender de AbstractAnimalFactory(FactoryDecorator)
# class AnimalFactory:

#     @classmethod
#     @FactoryInterface.factory_method
#     def create_record(
#         cls, name: str, specie: str, weight: float, animal_type: str
#     ) -> Type[Animals]:
#         """Cria modelo de animal"""
#         defined_type = cls.__define_type(animal_type)

#         return Animals(
#             name=name,
#             specie=specie,
#             weight=weight,
#             animal_type=animal_type,
#             survival_strategy=defined_type['strategy'],
#             diet_validation=defined_type['validator']('food')
#         )


#     @classmethod
#     @FactoryInterface.factory_method
#     def create_validation_chain(cls, handler: str) -> Type[ValidationChain]:
#         """Define uma cadeia de responsabilidade de um serviço"""
#         return ValidationChain(
#             [
#                 HenValidator(handler),
#                 DogValidator(handler),
#                 CattleValidator(handler),
#                 PigValidator(handler),
#                 HorseValidator(handler),
#             ]
#         )


#     @classmethod
#     def __define_type(
#         cls, animal_type: str
#     ) -> Union[Dict[str, Type[AnimalStrategyInterface]], Dict[str, Type[ValidatorInterface]]]:
#         """Define as extensões para o tipo do animal"""
#         match animal_type:
#             case "hen":
#                 return {'strategy': HenStrategy, 'validator': HenValidator}
#             case "dog":
#                 return {'strategy': DogStrategy, 'validator': DogValidator}
#             case "cattle":
#                 return {'strategy': CattleStrategy, 'validator': CattleValidator}
#             case "pig":
#                 return {'strategy': PigStrategy, 'validator': PigValidator}
#             case "horse":
#                 return {'strategy': HorseStrategy, 'validator': HorseValidator}
#         return None