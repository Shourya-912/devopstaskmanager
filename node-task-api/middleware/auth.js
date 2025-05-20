
// middleware to verify JWT token
const jwt = require('jsonwebtoken');
 
function verifyToken(req, res, next) {
  const authHeader = req.headers['authorization'];
 
  if (!authHeader) return res.status(401).json({ error: 'Token missing' });
 
  try {
    const decoded = jwt.verify(authHeader.split(" ")[1], `${process.env.SECRET_KEY}`);
    console.log(decoded)
    
    req.userId = Number(decoded.sub || decoded.identity);  // Flask returns 'identity'

    next();
  } catch (err) {
    res.status(401).json({ error: 'Invalid or expired token' });
  
  };
}

module.exports = verifyToken;