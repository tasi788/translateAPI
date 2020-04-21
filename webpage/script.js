var vm = new Vue({
  el: "#app",
  data: {
    input: "",
    resp: [{
      "provider": "google",
      "status": true,
      "result": "文字"
    }]
  },
  methods: {
    async query() {
      this.resp = (await axios.post('http://localhost:8000/', {
        InputText: this.input
      })).data
    }
  },
});