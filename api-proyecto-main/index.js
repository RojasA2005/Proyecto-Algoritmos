const fs = require('fs');
const dayjs  = require('dayjs');
const { fakerES: faker } = require('@faker-js/faker');


let users = new Array(100).fill({}).map((_) => {
  const type = faker.helpers.arrayElement(['listener', 'musician']);
  const firstName = faker.person.firstName();
  const lastName = faker.person.lastName();
  const obj = {
    id: faker.string.uuid(),
    name: `${firstName} ${type === 'listener' ? lastName : ''}`,
    email: faker.internet.email({
      firstName: firstName.toLowerCase(),
      lastName: lastName.toLowerCase(),
      allowSpecialCharacters: false,
      provider: 'unimet.edu.ve',
    }),
    username: faker.internet.userName(),
    type,
  };
  // if (type === 'listener') {
  //   obj.major = faker.helpers.arrayElement([
  //     'Ingeniería Civil',
  //     'Ingeniería Eléctrica',
  //     'Ingeniería Mecánica',
  //     'Ingeniería de Producción',
  //     'Ingeniería Química',
  //     'Ingeniería de Sistemas',
  //     'Contaduría Publica',
  //     'Economía Empresarial',
  //     'Ciencias Administrativas',
  //     'Psicología',
  //     'Matematicas Industriales',
  //     'Idiomar Modernos',
  //     'Educación',
  //     'Derecho',
  //     'Estudios Liberales',
  //   ]);
  // } else {
  //   obj.department = faker.helpers.arrayElement([
  //     'Banca, Contabilidad y Auditoría',
  //     'Economía',
  //     'Gerencia y Emprendimiento',
  //     'Finanzas',
  //     'Mercadeo',
  //     'Ciencias de la Educación',
  //     'Ciencias del Comportamiento',
  //     'Desarrollo Integral',
  //     'Humanidades',
  //     'Física',
  //     'Inglés',
  //     'Lingüística',
  //     'Matemáticas',
  //     'Química',
  //     'Estudios Internacionales',
  //     'Estudios Jurídicos',
  //     'Estudios Políticos',
  //     'la Construcción y Desarrollo Sustentable',
  //     'Energía y Automatización',
  //     'Producción Industrial',
  //     'Gestión de Proyectos y Sistemas',
  //   ]);
  // }
  return obj;
});


const musicians = users.filter((obj) => obj.type ==='musician');
const listeners = users.filter((obj) => obj.type === 'listener');

const albums = new Array(300).fill({}).map((_) => {
  const name = faker.word.words(3);
  const obj = {
    id: faker.string.uuid(),
    name,
    description: faker.lorem.paragraphs(2),
    cover: faker.image.urlPlaceholder({
      height: 800,
      width: 800,
      text: name,
      format: 'jpg',
    }),
    published: faker.date.past().toISOString(),
    genre: faker.music.genre(),
    artist: faker.helpers.arrayElement(musicians).id,
    tracklist: new Array(faker.number.int({ min: 1, max: 12 }))
      .fill({})
      .map((_) => ({
        id: faker.string.uuid(),
        name: faker.word.words(3),
        duration: dayjs(
          new Date(
            2024,
            1,
            15,
            0,
            faker.number.int({ min: 1, max: 5 }),
            faker.number.int({ min: 0, max: 59 }),
            0
          )
        ).format('mm:ss'),
        link: faker.helpers.arrayElement([
          'https://soundcloud.com/luk_music/meduza-control-piece-edx-jaded?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/calvinharris/desire-with-sam-smith?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/luk_music/elderbrook-dababy-why-do-we-shake-in-the-cold-practice-luk-mashup-remix?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/luk_music/luk-feat-ellie-may-wicked-game?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/ginchiestrecords/ginchy-gxd-feat-yasmin-jane-as-the-rush-comes-radio-edit?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/jaxonmase/cola-x-ferrari-horses?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/jerzybulx/thebusiness?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/3uki/dua-lipa-houdini-3uki-remix?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/luk_music/luk-feat-kimberley-dont-cha-1?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
          'https://soundcloud.com/itsproppa/proppagfys?in=luk_music/sets/ibiza-techno-house-2024-summer-mix&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing',
        ]),
      })),
  };
  return obj;
});

const songs = albums.flatMap((obj) => obj.tracklist);

const playlists = new Array(100).fill({}).map((_) => {
  const obj = {
    id: faker.string.uuid(),
    name: faker.word.words(3),
    description: faker.lorem.paragraphs(2),
    creator: faker.helpers.arrayElement(listeners).id,
    tracks: new Array(faker.number.int({ min: 10, max: 100 })).fill({}).map((_) => faker.helpers.arrayElement(songs).id),
  };
  return obj;
});

fs.writeFileSync('./users.json', JSON.stringify(users, null, 2));
fs.writeFileSync('./albums.json', JSON.stringify(albums, null, 2));
fs.writeFileSync('./playlists.json', JSON.stringify(playlists, null, 2));
