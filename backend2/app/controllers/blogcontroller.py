from flask import request,jsonify
from prisma.models import Blog
from app.services.aigenerator import generateblog
from app.middleware.blogmid import auth_required

@auth_required
def generate():
    data=request.json
    url=data.get("videourl")
    print(url)
    if not url:
        return {"message":"Video URL is required"}
    blog=generateblog(url)
    if not blog:
        return {"message":"Error generating blog"}
    print(request.user["id"])
    Blog.prisma().create(
        data={"title": f"Blog from {url}", "content": blog, "userId": request.user["id"]}
    )
    print(blog)
    return jsonify({"blog": blog})