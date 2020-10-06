from rest_framework import serializers
from Voluntarios.models import Voluntirio, Estado, Cidade2, Cidade


class VoluntirioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voluntirio
        fields = '__all__'

class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'  
        
class Cidade2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade2
        fields = '__all__'           

    
    def create(self, validated_data):        
        produto = Voluntirio.objects.create(**validated_data)
        produto = Estado.objects.create(**validated_data)
        produto = Cidade.objects.create(**validated_data)
        produto = Cidade2.objects.create(**validated_data)

        return produto

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sobrenome = validated_data.get('sobrenome', instance.sobrenome)
        instance.bairro = validated_data.get('bairro', instance.bairro)
        instance.cidade = validated_data.get('cidade', instance.cidade)
        
        instance.save()
        return instance

