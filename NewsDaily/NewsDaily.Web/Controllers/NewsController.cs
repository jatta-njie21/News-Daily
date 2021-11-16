using Microsoft.AspNetCore.Mvc;
using NewsDaily.Web.Models;
using NewsDaily.Web.Services;

namespace NewsDaily.Web.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class NewsController : ControllerBase
    {

        public NewsController(JsonFileNewsService newsService)
        {
            NewsService = newsService;
        }
        public JsonFileNewsService NewsService { get; }

        [HttpGet]
        public IEnumerable<News> Get()
        {
            return NewsService.GetNews();
        }

    }

}
