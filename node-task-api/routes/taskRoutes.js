const express = require('express');
const router = express.Router();
const Task = require('../models/Task');
const axios = require('axios');
const auth = require('../middleware/auth')


//Create Task 
router.post('/createtask', auth, async (req, res) => {

    const {title, description} = req.body;
    const userId = req.userId; //injected from JWT

    const token = req.headers['authorization'];
    try{
        const userResponse = await axios.get(`http://localhost:5000/user/${userId}`, {headers: {
            Authorization: token     //pass the token to the flask 
        }
        });
        
        if (!userResponse.data){
            return res.status(400).json({error:"user not found"});
        }   
        const task = await Task.create({title, description,userId});
        res.status(201).json(task);

    }catch(err){
        res.status(400).json({error: err.message ||"failed to validate user or create task"});
    }
});


//get all tasks
router.get('/showusers', auth, async(req,res) => {
    
    const token = req.headers['authorization'];
    try{
        const userResponse = await axios.get(`http://localhost:5000/showusers`,{headers: {
            Authorization: token     //pass the token to the flask 
        }
        });
        
        if (!userResponse.data){
            return res.status(400).json({error:"user not found"});
        }
        const tasks = await Task.find();
        res.json(tasks);
    } catch(err){
        res.status(400).json({error: err.message ||"failed to find all user's task"});
    } 
});


//get single user
router.get('/user', auth, async (req, res) => {
    
    const token = req.headers['authorization'];
    const uId = req.userId; //injected from JWT
    try{
        const userResponse = await axios.get(`http://localhost:5000/user/${uId}`,{headers: {
            Authorization: token //pass the token to the flask
        }
        });

        if (!userResponse.data){
            return res.status(400).json({error:"user not found"});
        }
        const tasks = await Task.find({userId: uId});
        res.json(tasks);
    } catch(err){
        res.status(400).json({error: err.message || `Tasks not found for userId ${userId}`});
    }
});

//update Task
router.put('/updatetask', auth, async(req,res) => {

    const token = req.headers['authorization'];
    const uId = req.userId; //injected from JWT
    
    try{
        const userResponse = await axios.get(`http://localhost:5000/user/${uId}`,{headers: {
            Authorization: token //pass the token to the flask
        }
        });

        console.log(userResponse.data);
        if (!userResponse.data){
            return res.status(400).json({error:"user not found"});
        }

        const user = await Task.findOne({userId: uId});
        const updated = await Task.findByIdAndUpdate(user['_id'],
             req.body, {new: true});
             res.json(updated);
    }catch(err){
        res.status(400).json({error: err.message});
    }
});


//Delete Task
router.delete('/delete', auth, async (req, res) => {
    

    const token = req.headers['authorization'];
    const uId = req.userId; //injected from JWT
    
    try{
        const userResponse = await axios.get(`http://localhost:5000/user/${uId}`,{headers: {
            Authorization: token //pass the token to the flask
        }
        });

        console.log(userResponse.data);
        if (!userResponse.data){
            return res.status(400).json({error:"user not found"});
        }
        
        const user = await Task.findOne({userId: uId});

        const updated = await Task.findByIdAndDelete(user['_id']);
        res.json({message: 'Task deleted'});
    }catch (err){
        res.status(400).json({error: err.message});
    }
});


module.exports = router;