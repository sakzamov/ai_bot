
import discord
from discord.ext import commands
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def bird_image(image, model_path, labels_path):
    # отключаем научную нотацию
    np.set_printoptions(suppress=True)
    # загружаем модель
    model = load_model(model_path, compile=False)
    # загружаем лейблы (названия классов)
    class_names = open(labels_path, "r", encoding='utf-8').readlines()
    # создаем массив нужной формы (нужна для подачи на вход модели в будущем)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # загрузка картинки
    image = Image.open(image).convert("RGB")
    # изменяем размеры изображения
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    # преобразование изображения к массиву
    image_array = np.asarray(image)
    # нормализация изображения (убираем шумы)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # в массив подставляем нормализированное изображение
    data[0] = normalized_image_array
    # получаем предсказание модели
    prediction = model.predict(data)
    # получаем индексч с наивысшим предсказанием класса
    index = np.argmax(prediction)
    # получаем имя класса
    class_name = class_names[index]
    # получаем вероятность этого класса
    confidence_score = prediction[0][index]
    # возвращем результат
    return class_name[2:], confidence_score



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            await i.save(f'./{file_name}')
            clas, p = bird_image(f'./{file_name}', 'keras_model.h5', 'labels.txt')
            if clas == 'Мерс\n':
                ctx.send('Это машина Мерс.Он любит бензин.')
            elif clas == 'Лада\n':
                await ctx.send('Это машина Лада.Она любит бензин.')
            elif clas == 'Фера\n':
                await ctx.send('Это машина Фера.Она любит бензин.')
            elif clas == 'Фиат\n':
                await ctx.send('Это машина Фиат.Он любит бензин.')
            elif clas == 'Гелик\n':
                await ctx.send('Это машина Гелик.Он любит бензин.')
            elif clas == 'Мазда\n':
                await ctx.sendx.send('Это машина Мазда.Она любит бензин.')
            elif clas == 'Ламба\n':
                await ctx.send('Это машина Ламба.Она любит бензин.')
            elif clas == 'Фольксваген\n':
                await ctx.send('Это машина Фольксваген.Он любит бензин.')
            elif clas == 'Хонда\n':
                await ctx.send('Это машина Хонда.Она любит бензин.')
            elif clas == 'Хёндай\n':
                await ctx.send('Это машина Хёндай.Он любит бензин.')
            elif clas == 'Тойота\n':
                await ctx.send('Это машина Тойота.Она любит бензин.')
            elif clas == 'Форд\n':
                await ctx.send('Это машина Форд.Он любит бензин.')
            elif clas == 'Рено\n':
                await ctx.send('Это машина Рено.Он любит бензин.')
            elif clas == 'Опель\n':
                await ctx.send('Это машина Опель.Он любит бензин.')
            elif clas == 'Джип\n':
                await ctx.send('Это машина Джип.Он любит бензин.')
            elif clas == 'Митсубиши\n':
                await ctx.send('Это машина Митсубиши.Он любит бензин.')
            elif clas == 'Киа\n':
                await ctx.send('Это машина Киа.Она любит бензин.')
            elif clas == 'БМВ\n':
                await ctx.send('Это машина БМВ.Он любит бензин.')
            elif clas == 'Лексус\n':
                await ctx.send('Это машина Лексус.Он любит бензин.')
            elif clas == 'Ниссан\n':
                await ctx.send('Это машина Ниссан.Он любит бензин.')
    else:
        await ctx.send('Вложение не было')        

bot.run('MTE1MjkwNDQyNTI0NjAzNjA3OQ.GV51IT.2dClOoC7cuilIVMWJNHBARDxpJYujnofl5Wp0w')