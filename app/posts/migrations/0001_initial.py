# Generated by Django 3.0.5 on 2020-04-28 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='포함 항목 물품')),
            ],
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=30, null=True, verbose_name='회사 명')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='주소')),
                ('managerName', models.CharField(max_length=30, null=True, verbose_name='중개인')),
                ('tel', models.CharField(max_length=13, null=True, verbose_name='전화번호')),
                ('image', models.ImageField(null=True, upload_to=posts.models.broker_image_path, verbose_name='이미지')),
                ('companyNumber', models.CharField(max_length=20, null=True, verbose_name='사업자 번호')),
                ('brokerage', models.CharField(max_length=30, null=True, verbose_name='중개등록번호')),
                ('dabangCreated_at', models.CharField(max_length=20, null=True, verbose_name='다방 가입일')),
                ('successCount', models.CharField(max_length=20, null=True, verbose_name='거래 성공 횟수')),
            ],
        ),
        migrations.CreateModel(
            name='ComplexInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complexName', models.CharField(max_length=30, null=True, verbose_name='단지 이름')),
                ('buildDate', models.CharField(max_length=20, null=True, verbose_name='설립 날짜')),
                ('totalCitizen', models.CharField(max_length=20, null=True, verbose_name='총 세대 수')),
                ('personalPark', models.CharField(max_length=10, null=True, verbose_name='주차 대수')),
                ('totalNumber', models.CharField(max_length=10, null=True, verbose_name='총 동 수')),
                ('heatingSystem', models.CharField(max_length=15, null=True, verbose_name='난방 방식')),
                ('minMaxFloor', models.CharField(max_length=10, null=True, verbose_name='최저-최고 층')),
                ('buildingType', models.CharField(max_length=10, null=True, verbose_name='건물 유형')),
                ('constructionCompany', models.CharField(max_length=30, null=True, verbose_name='건설사')),
                ('fuel', models.CharField(max_length=10, null=True, verbose_name='연로')),
                ('complexType', models.CharField(max_length=10, null=True, verbose_name='단지 타입')),
                ('floorAreaRatio', models.CharField(max_length=10, null=True, verbose_name='용적률')),
                ('dryWasteRate', models.CharField(max_length=10, null=True, verbose_name='건폐율')),
                ('complexSale', models.CharField(max_length=10, null=True, verbose_name='단지 평당가 매매 ')),
                ('complexPrice', models.CharField(max_length=10, null=True, verbose_name='단지 평당가 전세 ')),
                ('areaSale', models.CharField(max_length=30, null=True, verbose_name='이 지역 평당가 매매')),
                ('areaPrice', models.CharField(max_length=30, null=True, verbose_name='이 지역 평당가 전세')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalFee', models.FloatField(verbose_name='관리비 합계')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.AdministrativeDetail', verbose_name='포함 항목')),
            ],
        ),
        migrations.CreateModel(
            name='OptionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='옵션 항목 아이템')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='옵션 이미지')),
            ],
        ),
        migrations.CreateModel(
            name='PostAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loadAddress', models.CharField(max_length=50, null=True)),
                ('detailAddress', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, null=True, verbose_name='매물 종류')),
                ('description', models.TextField(max_length=500, verbose_name='설명')),
                ('lat', models.FloatField(null=True, verbose_name='x축')),
                ('lng', models.FloatField(null=True, verbose_name='y축')),
                ('floor', models.CharField(max_length=5, null=True, verbose_name='층 수')),
                ('totalFloor', models.CharField(max_length=5, null=True, verbose_name='건물 층 수')),
                ('areaChar', models.CharField(max_length=20, null=True, verbose_name='문자형 전용 면적')),
                ('supplyAreaInt', models.IntegerField(verbose_name='정수형 공급 면적')),
                ('supplyAreaChar', models.CharField(max_length=10, null=True, verbose_name='문자형 공급 면적')),
                ('shortRent', models.NullBooleanField(default=None, verbose_name='단기임대')),
                ('parkingDetail', models.CharField(max_length=10, null=True, verbose_name='주차 비용')),
                ('parkingTF', models.NullBooleanField(default=None, verbose_name='주차 가능 유무')),
                ('parkingPay', models.FloatField(null=True, verbose_name='주차 비용')),
                ('living_expenses', models.CharField(max_length=15, null=True, verbose_name='생활비')),
                ('living_expenses_detail', models.CharField(max_length=20, null=True, verbose_name='생활비 항목')),
                ('moveInChar', models.CharField(max_length=10, null=True, verbose_name='크롤링용 입주날짜')),
                ('moveInDate', models.DateTimeField(null=True, verbose_name='입주 가능 날짜')),
                ('heatingType', models.CharField(max_length=10, verbose_name='난방 종류')),
                ('pet', models.NullBooleanField(default=None, verbose_name='반려동물')),
                ('elevator', models.NullBooleanField(default=None, verbose_name='엘레베이터')),
                ('builtIn', models.NullBooleanField(default=None, verbose_name='빌트인')),
                ('veranda', models.NullBooleanField(default=None, verbose_name='베란다/ 발코니')),
                ('depositLoan', models.NullBooleanField(default=None, verbose_name='전세 자금 대출')),
                ('totalCitizen', models.CharField(max_length=10, null=True, verbose_name='총 세대 수')),
                ('totalPark', models.CharField(max_length=10, null=True, verbose_name='세대당 주차 대수')),
                ('complete', models.CharField(max_length=10, null=True, verbose_name='준공 년 월')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.PostAddress')),
                ('broker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Broker')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.ComplexInformation', verbose_name='단지')),
                ('management', models.ManyToManyField(through='posts.MaintenanceFee', to='posts.AdministrativeDetail')),
            ],
        ),
        migrations.CreateModel(
            name='SalesForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='매물 종류')),
                ('depositChar', models.CharField(max_length=10, null=True, verbose_name='문자형 매매-보증금')),
                ('monthlyChar', models.CharField(max_length=10, null=True, verbose_name='문자형 월세')),
                ('depositInt', models.IntegerField(null=True, verbose_name='정수형 매매-보증금')),
                ('monthlyInt', models.IntegerField(null=True, verbose_name='정수형 월세')),
            ],
        ),
        migrations.CreateModel(
            name='SecuritySafetyFacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='보안/안전 시설 아이템')),
                ('image', models.ImageField(null=True, upload_to=posts.models.security_image_path, verbose_name='시설 이미지')),
            ],
        ),
        migrations.CreateModel(
            name='RoomSecurity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('postRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='securitySafety_set', to='posts.PostRoom', verbose_name='해당 매물')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.SecuritySafetyFacilities', verbose_name='보안 안전 시설')),
            ],
        ),
        migrations.CreateModel(
            name='RoomOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='optionname_set', to='posts.OptionItem', verbose_name='해당 옵션')),
                ('postRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_set', to='posts.PostRoom', verbose_name='해당 매물')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=posts.models.recommend_image_path, verbose_name='추천 단지 이미지')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='추천 단지 명')),
                ('type', models.CharField(max_length=20, null=True, verbose_name='추천 단지 아파트 타입')),
                ('totalCitizen', models.CharField(max_length=30, null=True, verbose_name='추천 단지 총 세대 수')),
                ('buildDate', models.CharField(max_length=20, null=True, verbose_name='추천 단지 설립일자')),
                ('address', models.CharField(max_length=20, null=True, verbose_name='추천 단지 주소')),
                ('link', models.CharField(max_length=100, null=True, verbose_name='추천 단지 링크')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.ComplexInformation', verbose_name='단지')),
            ],
        ),
        migrations.AddField(
            model_name='postroom',
            name='option',
            field=models.ManyToManyField(through='posts.RoomOption', to='posts.OptionItem', verbose_name='옵션 항목'),
        ),
        migrations.AddField(
            model_name='postroom',
            name='salesForm',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.SalesForm'),
        ),
        migrations.AddField(
            model_name='postroom',
            name='securitySafety',
            field=models.ManyToManyField(through='posts.RoomSecurity', to='posts.SecuritySafetyFacilities'),
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.PostRoom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=posts.models.post_image_path, verbose_name='방 이미지')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postimage_set', to='posts.PostRoom', verbose_name='해당 게시글')),
            ],
        ),
        migrations.AddField(
            model_name='maintenancefee',
            name='postRoom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='management_set', to='posts.PostRoom', verbose_name='해당 매물'),
        ),
        migrations.CreateModel(
            name='ComplexImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=posts.models.complex_image_path, verbose_name='방 이미지')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.ComplexInformation', verbose_name='단지 정보')),
            ],
        ),
    ]
