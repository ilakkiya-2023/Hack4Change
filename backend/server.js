

// const express = require('express');
// const multer = require('multer');
// const mongoose = require('mongoose');
// const path = require('path');

// const app = express();
// const port = 5000;

// mongoose.connect('mongodb+srv://Hack4Change:sign_language_forum@cluster0.l1pjkvd.mongodb.net/sign_language?retryWrites=true&w=majority&appName=Cluster0', {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// });

// const videoSchema = new mongoose.Schema({
//   username: String,
//   description: String,
//   videoPath: String,
// });

// const Video = mongoose.model('Video', videoSchema);

// const storage = multer.diskStorage({
//   destination: (req, file, cb) => {
//     cb(null, 'uploads');
//   },
//   filename: (req, file, cb) => {
//     cb(null, `${Date.now()}_${file.originalname}`);
//   },
// });

// const upload = multer({ storage });

// app.use(express.json());
// app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// app.post('/upload', upload.single('file'), (req, res) => {
//   const { username, description } = req.body;
//   const newVideo = new Video({
//     username,
//     description,
//     videoPath: `/uploads/${req.file.filename}`,
//   });

//   newVideo.save()
//     .then(() => res.status(200).send('Video uploaded successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.get('/videos', (req, res) => {
//   Video.find()
//     .then(videos => res.json(videos))
//     .catch(err => res.status(500).send(err.message));
// });

// app.delete('/videos/:id', (req, res) => {
//   Video.findByIdAndDelete(req.params.id)
//     .then(() => res.status(200).send('Video deleted successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.listen(port, () => {
//   console.log(`Server is running on port ${port}`);
// });


// ////////////////////////////////////////////////////////////////////////////////////////////////////////


// const express = require('express');
// const multer = require('multer');
// const mongoose = require('mongoose');
// const path = require('path');

// const app = express();
// const port = 5000;

// mongoose.connect('mongodb+srv://Hack4Change:sign_language_forum@cluster0.l1pjkvd.mongodb.net/sign_language?retryWrites=true&w=majority&appName=Cluster0', {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// });

// const videoSchema = new mongoose.Schema({
//   username: String,
//   description: String,
//   videoPath: String,
// });

// const Video = mongoose.model('Video', videoSchema);

// const storage = multer.diskStorage({
//   destination: (req, file, cb) => {
//     cb(null, 'uploads');
//   },
//   filename: (req, file, cb) => {
//     cb(null, `${Date.now()}_${file.originalname}`);
//   },
// });

// const upload = multer({ storage });

// app.use(express.json());
// app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// app.post('/upload', upload.single('file'), (req, res) => {
//   const { username, description } = req.body;
//   const newVideo = new Video({
//     username,
//     description,
//     videoPath: `/uploads/${req.file.filename}`,
//   });

//   newVideo.save()
//     .then(() => res.status(200).send('Video uploaded successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.get('/videos', (req, res) => {
//   Video.find()
//     .then(videos => res.json(videos))
//     .catch(err => res.status(500).send(err.message));
// });

// app.delete('/videos/:id', (req, res) => {
//   Video.findByIdAndDelete(req.params.id)
//     .then(() => res.status(200).send('Video deleted successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.listen(port, () => {
//   console.log(`Server is running on port ${port}`);
// });

// ////////////////////////////////////////////////////////////////////////////////////////////////////////


// const express = require('express');
// const multer = require('multer');
// const mongoose = require('mongoose');
// const path = require('path');

// const app = express();
// const port = 5000;

// mongoose.connect('mongodb+srv://Hack4Change:sign_language_forum@cluster0.l1pjkvd.mongodb.net/sign_language?retryWrites=true&w=majority&appName=Cluster0', {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// });

// const videoSchema = new mongoose.Schema({
//   username: String,
//   description: String,
//   videoPath: String,
// });

// const materialSchema = new mongoose.Schema({
//   description: String,
//   videoPath: String,
// });

// const Video = mongoose.model('Video', videoSchema);
// const Material = mongoose.model('Material', materialSchema);

// const storage = multer.diskStorage({
//   destination: (req, file, cb) => {
//     cb(null, 'uploads');
//   },
//   filename: (req, file, cb) => {
//     cb(null, `${Date.now()}_${file.originalname}`);
//   },
// });

// const upload = multer({ storage });

// app.use(express.json());
// app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// // Video endpoints
// app.post('/upload', upload.single('file'), (req, res) => {
//   const { username, description } = req.body;
//   const newVideo = new Video({
//     username,
//     description,
//     videoPath: `/uploads/${req.file.filename}`,
//   });

//   newVideo.save()
//     .then(() => res.status(200).send('Video uploaded successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.get('/videos', (req, res) => {
//   Video.find()
//     .then(videos => res.json(videos))
//     .catch(err => res.status(500).send(err.message));
// });

// app.delete('/videos/:id', (req, res) => {
//   Video.findByIdAndDelete(req.params.id)
//     .then(() => res.status(200).send('Video deleted successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// // Learning materials endpoints
// app.post('/materials', upload.single('file'), (req, res) => {
//   const { description } = req.body;
//   const newMaterial = new Material({
//     description,
//     videoPath: `/uploads/${req.file.filename}`,
//   });

//   newMaterial.save()
//     .then(() => res.status(200).send('Material uploaded successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.get('/materials', (req, res) => {
//   Material.find()
//     .then(materials => res.json(materials))
//     .catch(err => res.status(500).send(err.message));
// });

// app.delete('/materials/:id', (req, res) => {
//   Material.findByIdAndDelete(req.params.id)
//     .then(() => res.status(200).send('Material deleted successfully'))
//     .catch(err => res.status(500).send(err.message));
// });

// app.listen(port, () => {
//   console.log(`Server is running on port ${port}`);
// });




const express = require('express');
const multer = require('multer');
const mongoose = require('mongoose');
const path = require('path');

const app = express();
const port = 5000;

mongoose.connect('mongodb+srv://Hack4Change:sign_language_forum@cluster0.l1pjkvd.mongodb.net/sign_language?retryWrites=true&w=majority&appName=Cluster0', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const videoSchema = new mongoose.Schema({
  username: String,
  description: String,
  videoPath: String,
});

const materialSchema = new mongoose.Schema({
  description: String,
  videoPath: String,
});

const Video = mongoose.model('Video', videoSchema);
const Material = mongoose.model('Material', materialSchema);

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}_${file.originalname}`);
  },
});

const upload = multer({ storage });

app.use(express.json());
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Video endpoints
app.post('/upload', upload.single('file'), (req, res) => {
  const { username, description } = req.body;
  const filePath = `/uploads/${req.file.filename}`;

  console.log(`Uploading video: ${filePath}`); // Debugging line

  const newVideo = new Video({
    username,
    description,
    videoPath: filePath,
  });

  newVideo.save()
    .then(() => res.status(200).send('Video uploaded successfully'))
    .catch(err => res.status(500).send(err.message));
});

app.get('/videos', (req, res) => {
  Video.find()
    .then(videos => res.json(videos))
    .catch(err => res.status(500).send(err.message));
});

app.delete('/videos/:id', (req, res) => {
  Video.findByIdAndDelete(req.params.id)
    .then(() => res.status(200).send('Video deleted successfully'))
    .catch(err => res.status(500).send(err.message));
});

// Learning materials endpoints
app.post('/materials', upload.single('file'), (req, res) => {
  const { description } = req.body;
  const filePath = `/uploads/${req.file.filename}`;

  console.log(`Uploading material: ${filePath}`); // Debugging line

  const newMaterial = new Material({
    description,
    videoPath: filePath,
  });

  newMaterial.save()
    .then(() => res.status(200).send('Material uploaded successfully'))
    .catch(err => res.status(500).send(err.message));
});

app.get('/materials', (req, res) => {
  Material.find()
    .then(materials => res.json(materials))
    .catch(err => res.status(500).send(err.message));
});

app.delete('/materials/:id', (req, res) => {
  Material.findByIdAndDelete(req.params.id)
    .then(() => res.status(200).send('Material deleted successfully'))
    .catch(err => res.status(500).send(err.message));
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
