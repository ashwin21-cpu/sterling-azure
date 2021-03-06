# Generated by Django 3.0.6 on 2021-03-16 06:53

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residential_address1', models.TextField(blank=True, null=True)),
                ('residential_address2', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('is_company', models.BooleanField(default=False)),
                ('is_firm', models.BooleanField(default=False)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('firm_name', models.CharField(blank=True, max_length=50, null=True)),
                ('person_name', models.CharField(blank=True, max_length=50, null=True)),
                ('person_relation', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.TextField()),
                ('date', models.DateField(db_index=True)),
            ],
            options={
                'db_table': 'holidays',
            },
        ),
        migrations.CreateModel(
            name='IdentityDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('ssn', models.CharField(blank=True, max_length=50, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('dependents', models.CharField(blank=True, max_length=5, null=True)),
                ('investment_experience', models.CharField(blank=True, max_length=50, null=True)),
                ('employment_status', models.CharField(blank=True, max_length=50, null=True)),
                ('accountno', models.TextField(blank=True, null=True)),
                ('pancard', models.TextField(blank=True, null=True)),
                ('aadharcard', models.TextField(blank=True, null=True)),
                ('buyingpower', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('portfolio_value', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.CharField(blank=True, max_length=100, null=True)),
                ('ticker', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(default=0)),
                ('price', models.FloatField(blank=True, null=True)),
                ('ordertype', models.CharField(blank=True, max_length=100, null=True)),
                ('unrealised_gainloss', models.IntegerField(blank=True, default=0, null=True)),
                ('margin', models.CharField(blank=True, max_length=100, null=True)),
                ('interest', models.FloatField(blank=True, null=True)),
                ('equity', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 12, 23, 13, 226801), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockGeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(db_index=True, max_length=20)),
                ('market_cap', models.FloatField(blank=True, default=None, null=True)),
                ('average_volume', models.FloatField(blank=True, default=None, null=True)),
                ('currency', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('founded', models.IntegerField(blank=True, default=None, null=True)),
                ('industry', models.TextField(blank=True, default=None, null=True)),
                ('sector', models.TextField(blank=True, default=None, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('ipo_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('employees', models.IntegerField(blank=True, default=None, null=True)),
                ('ceo', models.TextField(blank=True, default=None, null=True)),
                ('city', models.TextField(blank=True, default=None, null=True)),
                ('state', models.TextField(blank=True, default=None, null=True)),
                ('country', models.TextField(blank=True, default=None, null=True)),
                ('price_earning_ratio', models.FloatField(blank=True, default=None, null=True)),
                ('dividend_yield', models.FloatField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'stock_general_info',
            },
        ),
        migrations.CreateModel(
            name='StockNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True, db_index=True, null=True)),
                ('token', models.TextField(blank=True, null=True)),
                ('isin', models.TextField(blank=True, default=None, null=True)),
                ('series', models.TextField(blank=True, default=None, null=True)),
                ('date_of_listing', models.DateTimeField(blank=True, default=None, null=True)),
                ('paid_up', models.TextField(blank=True, default=None, null=True)),
                ('market', models.TextField(blank=True, default=None, null=True)),
                ('face_value', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZerodhaCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credentials', models.TextField()),
                ('login_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'zerodha_creds',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.BasicDetails')),
                ('identity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_identity_rel', to='accounts.IdentityDetails')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_number', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 12, 23, 13, 228059), null=True)),
                ('position_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='histroy_position_rel', to='accounts.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 12, 23, 13, 226015), null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('ordertype', models.TextField(blank=True, null=True)),
                ('expires', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('limit_price', models.FloatField(blank=True, null=True)),
                ('status', models.TextField(blank=True, choices=[('pending', 'pending'), ('executed', 'executed')], db_index=True, default='pending', null=True)),
                ('remove_date', models.DateTimeField(blank=True, null=True)),
                ('transaction_type', models.CharField(default='buy', max_length=10)),
                ('stockticker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_transaction_rel', to='accounts.StockNames')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_rel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'index_together': {('expires', 'status', 'time'), ('userid', 'stockticker', 'status')},
            },
        ),
        migrations.CreateModel(
            name='TotalGainLoss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gainloss', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 12, 23, 13, 228410), null=True)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_total_gl_rel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(db_index=True)),
                ('price', models.FloatField()),
                ('token', models.CharField(db_index=True, max_length=20)),
                ('symbol', models.CharField(db_index=True, max_length=20)),
            ],
            options={
                'db_table': 'stock_prices',
                'index_together': {('symbol', 'time_stamp')},
            },
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailing_pe', models.FloatField(blank=True, null=True)),
                ('market_cap', models.FloatField(blank=True, null=True)),
                ('price_to_book', models.FloatField(blank=True, null=True)),
                ('company_info', models.TextField(blank=True, null=True)),
                ('officers', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('employees', models.CharField(blank=True, max_length=500, null=True)),
                ('headquaters', models.CharField(blank=True, max_length=500, null=True)),
                ('pe_ratio', models.CharField(blank=True, max_length=500, null=True)),
                ('open_price', models.CharField(blank=True, max_length=500, null=True)),
                ('low_today', models.CharField(blank=True, max_length=500, null=True)),
                ('high_today', models.CharField(blank=True, max_length=500, null=True)),
                ('sector', models.CharField(blank=True, max_length=500, null=True)),
                ('stock', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_info', to='accounts.StockNames')),
            ],
        ),
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('current_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('last_update', models.DateField(blank=True, null=True)),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='accounts.StockNames')),
            ],
        ),
        migrations.CreateModel(
            name='StockGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GISC', models.CharField(blank=True, max_length=500, null=True)),
                ('Industry', models.CharField(blank=True, max_length=500, null=True)),
                ('ROE', models.CharField(blank=True, max_length=500, null=True)),
                ('PE', models.CharField(blank=True, max_length=500, null=True)),
                ('DE', models.CharField(blank=True, max_length=500, null=True)),
                ('GPM', models.CharField(blank=True, max_length=500, null=True)),
                ('companyname', models.CharField(blank=True, max_length=500, null=True)),
                ('Stockticker', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='general', to='accounts.StockNames')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='stockname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stockposition_rel', to='accounts.StockNames'),
        ),
        migrations.AddField(
            model_name='position',
            name='transaction_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stockposition_transaction_rel', to='accounts.Transaction'),
        ),
        migrations.AddField(
            model_name='position',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userposition_rel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Portolfio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.TextField(blank=True, null=True)),
                ('tensector', models.TextField(blank=True, null=True)),
                ('gainloss', models.TextField(blank=True, null=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_rel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GainLossChartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gainloss_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 12, 23, 13, 229347), null=True)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_gl_chart_data_rel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopSearched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_top_search_rel', to='accounts.StockNames')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_top_search_rel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'index_together': {('stock', 'userid')},
            },
        ),
        migrations.AlterIndexTogether(
            name='position',
            index_together={('userid', 'ticker'), ('userid', 'stockname')},
        ),
        migrations.CreateModel(
            name='PortfolioValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('portfolio_value', models.FloatField(default=0.0)),
                ('cash_balance', models.FloatField(default=0.0)),
                ('realized_gain_loss', models.FloatField(default=0.0)),
                ('unrealized_gain_loss', models.FloatField(default=0.0)),
                ('amount', models.FloatField(default=0.0)),
                ('deletable', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'portfolio_values',
                'index_together': {('user', 'timestamp')},
            },
        ),
        migrations.CreateModel(
            name='GainLossHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unrealised_gainloss', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('realised_gainloss', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('total_cash', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('is_calculated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 12, 23, 13, 228824), null=True)),
                ('position_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gl_history_position_rel', to='accounts.Position')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_gl_history_rel', to='accounts.StockNames')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_gl_history_rel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'index_together': {('userid', 'stock')},
            },
        ),
    ]
