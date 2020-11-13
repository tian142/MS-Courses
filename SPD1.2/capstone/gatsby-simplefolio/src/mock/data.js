import { nanoid } from 'nanoid';

// HEAD DATA
export const headData = {
  title: 'Tian | Developer', // e.g: 'Name | Developer'
  lang: '', // e.g: en, es, fr, jp
  description: '', // e.g: Welcome to my website
};

// HERO DATA
export const heroData = {
  title: 'Hi, my name is',
  name: 'Tian Qiu',
  subtitle: "I'm a software enginnerer.",
  cta: '',
};

// ABOUT DATA
export const aboutData = {
  img: 'tian.jpg',
  paragraphOne:
    'I am an autodidact, value-driven software engineer who wants to use software to solve problems in my life and the lives of people with similar problems.',
  paragraphTwo: ' I am interested in and working on projects related to the social gaming space.',
  paragraphThree: '',
  resume: 'https://www.linkedin.com/in/tian-qiu-91bb8a127/', // if no resume, the button will not show up
};

// PROJECTS DATA
export const projectsData = [
  {
    id: nanoid(),
    img: 'love-calc.PNG',
    title: 'Love Calculator',
    info:
      'Find out the algorithmically calculated compatibility score bewteen two individuals, tech used: React(frontend), Rapidapi(api calls), and Firebase(hosting). ',
    info2: '',
    url: 'https://love-calculator-b1e95.firebaseapp.com/',
    repo: 'https://github.com/tian142/Love-Calculator', // if no repo, the button will not show up
  },
  {
    id: nanoid(),
    img: 'mood-shop.PNG',
    title: 'Mood Shopping Cart',
    info:
      'A shop-front built from scratch using html, css, and javascript. This site has the functionality to add, subtract, remove, and enter custom amount of items into the shopping cart. ',
    info2: '',
    url: 'https://tian142.github.io/mood-shop/',
    repo: 'https://github.com/tian142/mood-shop', // if no repo, the button will not show up
  },
  {
    id: nanoid(),
    img: 'project.jpg',
    title: 'Large Social Media Project(work in progress)',
    info:
      'this project is still work in progress, I am learning Firebase Firestore and Cloud Functions to make a CRUD Social Media App, will provide more information once an MVP becomes presentable.',
    info2: '',
    url: '',
    repo: '', // if no repo, the button will not show up
  },
];

// CONTACT DATA
export const contactData = {
  cta: '',
  btn: '',
  email: '',
};

// FOOTER DATA
export const footerData = {
  networks: [
    {
      id: nanoid(),
      name: 'twitter',
      url: 'https://twitter.com',
    },
    {
      id: nanoid(),
      name: 'codepen',
      url: 'https://codepen.io',
    },
    {
      id: nanoid(),
      name: 'linkedin',
      url: 'https://www.linkedin.com/in/tian-qiu-91bb8a127/',
    },
    {
      id: nanoid(),
      name: 'github',
      url: 'https://github.com/tian142',
    },
  ],
};

// Github start/fork buttons
export const githubButtons = {
  isEnabled: true, // set to false to disable the GitHub stars/fork buttons
};
