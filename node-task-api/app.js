const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const taskRoutes = require('./routes/taskRoutes');

dotenv.config();
const app = express();
app.use(express.json());

mongoose.connect(process.env.MONGODB_URL,{
    useNewUrlParser:true,
    useUnifiedTopology:true
}).then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:',err))


//routes
app.use('/tasks',taskRoutes)

//start server
const PORT = process.env.PORT || 3000;
app.listen(PORT,'0.0.0.0' () => {
    console.log(`server running on port ${PORT}`);
});
