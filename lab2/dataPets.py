import os, shutil

# Путь к исходным данным
original_dataset_dir = 'D:\\pyProj\\lab2\\dataset\\pets'

# Каталог для сохранения небольшого набора данных
base_dir = 'D:\\pyProj\\lab2\\dataset\\pets_small'
os.mkdir(base_dir)

# Каталоги для обучающего, проверочного и контрольного поднаборов
train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

# Каталог для обучающих изображений
train_cats_dir = os.path.join(train_dir, 'catsPets')
os.mkdir(train_cats_dir)

train_dogs_dir = os.path.join(train_dir, 'dogsPets')
os.mkdir(train_dogs_dir)

# Каталог для проверочных изображения
validation_cats_dir = os.path.join(validation_dir, 'catsPets')
os.mkdir(validation_cats_dir)

validation_dogs_dir = os.path.join(validation_dir, 'dogsPets')
os.mkdir(validation_dogs_dir)

# Каталог для контрольных изображений
test_cats_dir = os.path.join(test_dir, 'catsPets')
os.mkdir(test_cats_dir)

test_dogs_dir = os.path.join(test_dir, 'dogsPets')
os.mkdir(test_dogs_dir)

fnames = ['cat{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(train_cats_dir, fname)
 shutil.copyfile(src, dst)

fnames = ['cat{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(validation_cats_dir, fname)
 shutil.copyfile(src, dst)

fnames = ['cat{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(test_cats_dir, fname)
 shutil.copyfile(src, dst)

fnames = ['dog{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(train_dogs_dir, fname)
 shutil.copyfile(src, dst)

fnames = ['dog{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(validation_dogs_dir, fname)
 shutil.copyfile(src, dst)

fnames = ['dog{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(test_dogs_dir, fname)
 shutil.copyfile(src, dst)

print('total training cat images:', len(os.listdir(train_cats_dir)))
print('total training dog images:', len(os.listdir(train_dogs_dir)))
print('total validation cat images:', len(os.listdir(validation_cats_dir)))
print('total validation dog images:', len(os.listdir(validation_dogs_dir)))
print('total test cat images:', len(os.listdir(test_cats_dir)))
print('total test dog images:', len(os.listdir(test_dogs_dir)))