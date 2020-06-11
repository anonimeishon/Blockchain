db.createUser({
  user: "block",
  pwd: "block",
  roles: [{ role: "readWrite", db: "blockchain" }]
})
